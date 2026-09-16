#!/usr/bin/env python3
"""
Migrate the Navitia Slate documentation to Docusaurus.

Idempotent: reads only from the pristine Slate sources and regenerates
docs/, static/img/ and the legacy hash-redirect map from scratch.

    python3 tools/migrate.py

Pipeline
  A. normalise headings   (setext / <hN id> / <a name>)  -> ATX + {#anchor}
  B. MDX-safety codemod   (<br>, autolinks, bare braces, asides, images)
  C. split into pages     (per PAGE_PLAN)
  D. index anchors, rewrite 319 in-page links to cross-page links
  E. emit static/legacy-redirects.json for the hash shim
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLATE = ROOT.parent / "Slate documentation" / "slate" / "source"
INCLUDES = SLATE / "includes"
DOCS = ROOT / "docs"
IMG = ROOT / "static" / "img"

# --------------------------------------------------------------------------
# Page plan.  split_on is the heading level whose occurrences start a new page.
# Sections smaller than `min_lines` are folded back into the preceding page.
# --------------------------------------------------------------------------

@dataclass
class Chapter:
    src: str                      # include file stem
    out: str                      # output dir (""=docs root) or single file path
    split_on: int | None = None   # heading level to split at; None = one page
    title: str | None = None      # override page title (single-page chapters)
    slug: str | None = None
    min_lines: int = 15
    position: int = 0
    category: str | None = None   # sidebar label when split_on is set
    overview: str = "overview"    # filename for the pre-first-heading preamble


PAGE_PLAN: list[Chapter] = [
    Chapter("welcome",          "getting-started",   title="Getting started", slug="/", position=1),
    Chapter("examples",         "examples",          title="Some examples",   position=2),
    Chapter("authentication",   "authentication",    title="Authentication",  position=3),
    Chapter("journey_planning", "features/journey-planning", title="Journey planning", position=1),
    Chapter("departures",       "features/next-departures",  title="Next departures and arrivals", position=2),
    Chapter("timetables",       "features/timetables",       title="Timetables", position=3),
    Chapter("nearby",           "features/places-nearby",    title="Places nearby", position=4),
    Chapter("explore",          "features/explore",          title="Explore transport", position=5),
    Chapter("isochrones",       "features/isochrones",       title="Isochrones", position=6),
    Chapter("interface",        "interface",         title="Interface", position=5),
    Chapter("apis",             "api",               split_on=2, category="API catalog", position=6),
    Chapter("objects",          "objects",           split_on=2, category="Objects", position=7),
    Chapter("realtime",         "real-time",         split_on=2, category="Real time", position=8, min_lines=20),
    Chapter("stuff",            "misc",              split_on=2, category="Misc mechanisms", position=9),
    Chapter("_errors",          "errors",            title="Errors", position=10),
    Chapter("lexicon",          "lexicon",           title="Lexicon", position=11),
]

CATEGORY_POSITION = {"features": 4, "api": 6, "objects": 7, "real-time": 8, "misc": 9}
CATEGORY_LABEL = {"features": "Features"}

# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------

FENCE = re.compile(r"^\s*```")
INLINE_CODE = re.compile(r"`[^`\n]*`")


def code_mask(lines: list[str]) -> list[bool]:
    """True for every line that is inside a fenced or indented code block."""
    mask, in_fence, prev_blank = [], False, True
    for ln in lines:
        if FENCE.match(ln):
            in_fence = not in_fence
            mask.append(True)
            continue
        if in_fence:
            mask.append(True)
        else:
            indented = (ln.startswith("    ") or ln.startswith("\t")) and prev_blank
            mask.append(indented)
            prev_blank = not ln.strip() or indented
        if not in_fence:
            prev_blank = not ln.strip()
    return mask


def outside_code(text: str, fn):
    """Apply fn to the parts of a line that are not inline code spans."""
    out, last = [], 0
    for m in INLINE_CODE.finditer(text):
        out.append(fn(text[last:m.start()]))
        out.append(m.group(0))
        last = m.end()
    out.append(fn(text[last:]))
    return "".join(out)


_slug_strip = re.compile(r"[^\w\- ]+", re.UNICODE)


def slugify(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("*", "").replace("_", "")
    text = _slug_strip.sub("", text.lower())
    return re.sub(r"\s+", "-", text.strip())


# --------------------------------------------------------------------------
# Stage A - heading normalisation
# --------------------------------------------------------------------------

HTML_H = re.compile(r'^\s*<h([1-6])\s*(?:id\s*=\s*"?([^"\s>]+)"?)?\s*>(.*?)</h\1>\s*$', re.I)
A_NAME_SELF = re.compile(r'<a\s+name="([^"]+)"\s*></a>\s*')
A_NAME_WRAP = re.compile(r'<a\s+name="([^"]+)"\s*>(.*?)</a>')
SETEXT_H1 = re.compile(r"^=+\s*$")
SETEXT_H2 = re.compile(r"^-{2,}\s*$")


def normalise_headings(lines: list[str]) -> list[str]:
    mask = code_mask(lines)
    out: list[str] = []
    i = 0
    while i < len(lines):
        ln, raw = lines[i].rstrip("\n"), lines[i]
        if mask[i]:
            out.append(raw)
            i += 1
            continue

        # setext -> ATX (lookahead on the underline)
        if i + 1 < len(lines) and not mask[i + 1] and ln.strip() and not ln.startswith("#"):
            nxt = lines[i + 1].rstrip("\n")
            if SETEXT_H1.match(nxt):
                out.append(f"# {ln.strip()}\n")
                i += 2
                continue
            if SETEXT_H2.match(nxt) and not ln.lstrip().startswith(("|", "-", "*", ">")):
                out.append(f"## {ln.strip()}\n")
                i += 2
                continue

        # <hN id="x">Title</hN> -> ATX + {#x}
        m = HTML_H.match(ln)
        if m:
            level, anchor, title = int(m.group(1)), m.group(2), m.group(3).strip()
            title, inner = _extract_a_name(title)
            anchor = anchor or inner
            suffix = f" {{#{anchor}}}" if anchor else ""
            out.append(f"{'#' * level} {title}{suffix}\n")
            i += 1
            continue

        # ATX heading carrying an <a name="x"> anchor
        if ln.lstrip().startswith("#"):
            hm = re.match(r"^(#{1,6})\s+(.*)$", ln.strip())
            if hm:
                title, inner = _extract_a_name(hm.group(2).strip())
                suffix = f" {{#{inner}}}" if inner else ""
                out.append(f"{hm.group(1)} {title}{suffix}\n")
                i += 1
                continue

        out.append(raw)
        i += 1
    return out


def _extract_a_name(title: str) -> tuple[str, str | None]:
    anchor = None
    m = A_NAME_SELF.search(title)
    if m:
        anchor = m.group(1)
        title = A_NAME_SELF.sub("", title, count=1)
    else:
        m = A_NAME_WRAP.search(title)
        if m:
            anchor = m.group(1)
            title = A_NAME_WRAP.sub(r"\2", title, count=1)
    return title.strip(), anchor


# --------------------------------------------------------------------------
# Stage B - MDX safety
# --------------------------------------------------------------------------

ASIDE_OPEN = re.compile(r'^\s*<aside\s+class="(notice|warning|success)"\s*>\s*(.*)$', re.I)
# Block-level <ul>/<li> markup: Slate accepted unclosed <li>, MDX does not.
# Rewrite it as a real markdown list.  Inline <ul><li>..</li></ul> inside table
# cells stays untouched, because those lines start with "|".
UL_ONLY = re.compile(r"^\s*</?ul>\s*$", re.I)
LI_START = re.compile(r"^\s*<li>\s*(.*?)\s*(?:</li>)?\s*$", re.I)
ASIDE_CLOSE = re.compile(r"^(.*?)</aside>\s*$", re.I)
ADMONITION = {"notice": "note", "warning": "warning", "success": "tip"}
AUTOLINK = re.compile(r"<(https?://[^>]+)>")
BR_BAD = re.compile(r"</br\s*>", re.I)
BR_OPEN = re.compile(r"<br\s*>", re.I)
IMG_LINK = re.compile(r"(!\[[^\]]*\]\()([^)\s]+)(\))")

IMAGE_FILES = {p.name for p in (SLATE / "images").glob("*")} if (SLATE / "images").exists() else set()


# A bare URL in prose gets auto-linked, and backslash escapes are not honoured
# inside an auto-link -- so an escaped brace would render as a literal "\{".
# URL templates carrying {placeholders} become inline code instead, which needs
# no escaping and reads correctly.
BARE_TEMPLATE_URL = re.compile(r"(?<![(\[`])\bhttps?://[^\s<>()\[\]`]*\\\{[^\s<>()\[\]`]*")


def _prose_fixes(seg: str) -> str:
    seg = BR_BAD.sub("<br />", seg)
    seg = BR_OPEN.sub("<br />", seg)
    seg = AUTOLINK.sub(r"[\1](\1)", seg)
    # bare { that MDX would otherwise evaluate as a JS expression
    seg = re.sub(r"(?<!\\)\{", r"\\{", seg)
    # ...but an escape inside an auto-linked bare URL would render literally,
    # so those URL templates become inline code, which needs no escaping.
    seg = BARE_TEMPLATE_URL.sub(lambda m: "`" + m.group(0).replace("\\{", "{") + "`", seg)
    return seg


def _fix_image(m: re.Match) -> str:
    target = m.group(2)
    if target.startswith(("http://", "https://", "/img/")):
        return m.group(0)
    name = target.lstrip("/").split("/")[-1]
    if name in IMAGE_FILES:
        return f"{m.group(1)}/img/{name}{m.group(3)}"
    return m.group(0)


INLINE_ANCHOR = re.compile(r'<a\s+name="([^"]+)"\s*></a>')


def mdx_safety(lines: list[str]) -> list[str]:
    mask = code_mask(lines)
    out: list[str] = []
    aside_depth = 0
    for i, raw in enumerate(lines):
        if mask[i]:
            out.append(raw)
            continue
        ln = raw.rstrip("\n")

        if UL_ONLY.match(ln):
            continue
        li = LI_START.match(ln)
        if li:
            ln = "- " + li.group(1)

        # Admonition bodies must not be indented, or they render as code blocks.
        if aside_depth:
            ln = ln.lstrip()

        if aside_depth == 0:
            m = ASIDE_OPEN.match(ln)
            if m:
                kind, rest = ADMONITION[m.group(1).lower()], m.group(2)
                out.append(f":::{kind}\n\n")
                aside_depth = 1
                closing = ASIDE_CLOSE.match(rest)
                if closing:
                    body = closing.group(1).strip()
                    if body:
                        out.append(outside_code(body, _prose_fixes) + "\n")
                    out.append("\n:::\n")
                    aside_depth = 0
                elif rest.strip():
                    out.append(outside_code(rest.strip(), _prose_fixes) + "\n")
                continue
        else:
            closing = ASIDE_CLOSE.match(ln)
            if closing:
                body = closing.group(1).strip()
                if body:
                    out.append(outside_code(body, _prose_fixes) + "\n")
                out.append("\n:::\n")
                aside_depth = 0
                continue

        ln = INLINE_ANCHOR.sub(r'<Anchor id="\1" />', ln)
        ln = IMG_LINK.sub(_fix_image, ln)
        ln = outside_code(ln, _prose_fixes)
        # heading anchors {#id} must survive the brace escaping
        ln = re.sub(r"\\\{#([^}]+)\}", r"{#\1}", ln)
        out.append(ln + "\n")
    return out


# --------------------------------------------------------------------------
# Stage C - split into pages
# --------------------------------------------------------------------------

ATX = re.compile(r"^(#{1,6})\s+(.*?)(?:\s*\{#([^}]+)\})?\s*$")


@dataclass
class Page:
    path: str                 # docs-relative route, e.g. "api/journeys"
    title: str
    body: list[str]
    position: int = 0
    slug: str | None = None
    anchors: list[str] = field(default_factory=list)


def parse_headings(lines: list[str]):
    mask = code_mask(lines)
    for i, ln in enumerate(lines):
        if mask[i]:
            continue
        m = ATX.match(ln.rstrip("\n"))
        if m:
            yield i, len(m.group(1)), m.group(2).strip(), m.group(3)


def split_chapter(ch: Chapter, lines: list[str]) -> list[Page]:
    if ch.split_on is None:
        title = ch.title or ch.src
        body, h1_anchor = strip_leading_h1(list(lines))
        page = Page(ch.out, title, body, ch.position, ch.slug)
        if h1_anchor:
            page.anchors.append(h1_anchor)
        return [page]

    heads = [h for h in parse_headings(lines) if h[1] == ch.split_on]
    pages: list[Page] = []
    pre = lines[: heads[0][0]] if heads else lines
    pre_body, h1_anchor = strip_leading_h1(pre)
    if [l for l in pre_body if l.strip()]:
        overview = Page(f"{ch.out}/{ch.overview}", chapter_title(lines) or ch.category or ch.src,
                        pre_body, 1)
        if h1_anchor:
            overview.anchors.append(h1_anchor)
        pages.append(overview)

    for n, (idx, _lvl, title, anchor) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        body = lines[idx + 1 : end]
        if len(body) < ch.min_lines and pages:
            pages[-1].body.extend(lines[idx:end])
            continue
        slug_name = anchor_to_filename(anchor, title)
        pages.append(Page(f"{ch.out}/{slug_name}", title, body, len(pages) + 1))
        if anchor:
            pages[-1].anchors.append(anchor)
    return pages


def strip_leading_h1(lines: list[str]) -> tuple[list[str], str | None]:
    """Drop a leading H1 (the frontmatter title renders it) and return its anchor."""
    for i, ln in enumerate(lines):
        if not ln.strip():
            continue
        m = ATX.match(ln.rstrip("\n"))
        if m and len(m.group(1)) == 1:
            return lines[i + 1 :], m.group(3)
        break
    return lines, None


def chapter_title(lines: list[str]) -> str | None:
    for i, lvl, title, _a in parse_headings(lines):
        if lvl == 1:
            return title
        break
    return None


_FILENAME_FIX = {
    "coord": "inverted-geocoding",
    "pt-ref": "public-transport-objects",
    "pt-objects": "autocomplete-pt-objects",
    "places": "autocomplete-places",
    "places-nearby-api": "places-nearby",
    "isochrones-api": "isochrones",
    "access-points-api": "access-points",
    "Freefloatings-nearby-api": "freefloatings-nearby",
    "PT_object_collections_data_freshness": "object-collections",
    "OTHER_EFFECT": "other-effect",
    "SIGNIFICANT_DELAYS": "trip-delayed",
    "REDUCED_SERVICE": "reduced-service",
    "NO_SERVICE": "no-service",
    "MODIFIED_SERVICE": "modified-service",
    "ADDITIONAL_SERVICE": "additional-service",
    "UNKNOWN_EFFECT": "unknown-effect",
    "Service-translation": "service-translation",
    "ridesharing-stuff": "ridesharing",
    "taxi-stuff": "taxi",
    "odt": "on-demand-transportation",
}


def anchor_to_filename(anchor: str | None, title: str) -> str:
    if anchor and anchor in _FILENAME_FIX:
        return _FILENAME_FIX[anchor]
    if anchor:
        return slugify(anchor.replace("_", "-"))
    return slugify(title)


# --------------------------------------------------------------------------
# Stage D - anchor index + link rewriting
# --------------------------------------------------------------------------

LINK = re.compile(r"\]\(#([^)]+)\)")
LINK_FULL = re.compile(r"\[([^\]]*)\]\(#([^)]+)\)")

# Anchors that no heading or <a name> ever defined -- these links are already
# broken on doc.navitia.io today.  We unlink them so the Docusaurus build is
# clean; the (self-describing) link text is preserved.  Fix in content, then
# delete from this list.
DEAD_ANCHORS = {
    "additional-informations",   # apis.md, stop_schedules field table
    "period-time",               # objects.md, disruption time_slots field
}


def page_level_anchors(pages: list[Page]) -> dict[str, str]:
    """Anchors whose heading became a page title, so they address a whole page.

    #journeys used to name a section of the single Slate page; it now names
    /api/journeys. Linking to /api/journeys#journeys would be a broken anchor,
    because that heading no longer exists in the body.
    """
    out: dict[str, str] = {}
    for page in pages:
        route = "/" + page.path
        for a in page.anchors:
            out.setdefault(a, route)
        title_slug = slugify(page.title)
        if title_slug:
            out.setdefault(title_slug, route)
    return out


def build_anchor_index(pages: list[Page]) -> dict[str, tuple[str, str | None]]:
    """Slate anchor id -> (docs route, fragment on that page).

    A fragment of None means the anchor addresses the whole page.

    Slate emitted two usable anchors per heading that carried an explicit id:
    the id itself and the slug of the heading text. Docusaurus emits only the
    explicit id, so both Slate spellings have to resolve to that one id.
    """
    index: dict[str, tuple[str, str | None]] = {}
    span_id = re.compile(r'<Anchor id="([^"]+)"')

    for anchor, route in page_level_anchors(pages).items():
        index[anchor] = (route, None)

    explicit: dict[str, tuple[str, str]] = {}
    auto: dict[str, tuple[str, str]] = {}
    for page in pages:
        route = "/" + page.path
        for line in page.body:
            for m in span_id.finditer(line):
                explicit.setdefault(m.group(1), (route, m.group(1)))
        seen: dict[str, int] = defaultdict(int)
        for _i, _lvl, title, anchor in parse_headings(page.body):
            s = slugify(title)
            if s:
                seen[s] += 1
                if seen[s] > 1:
                    s = f"{s}-{seen[s] - 1}"
            if anchor:
                explicit.setdefault(anchor, (route, anchor))
                if s:
                    # Slate also honoured the heading-text slug; redirect it
                    # onto the canonical id Docusaurus actually renders.
                    auto.setdefault(s, (route, anchor))
            elif s:
                auto.setdefault(s, (route, s))

    for src in (explicit, auto):
        for k, v in src.items():
            index.setdefault(k, v)
    return index


def rewrite_links(pages: list[Page], index: dict[str, tuple[str, str | None]]):
    fixed, broken = 0, []
    for page in pages:
        route = "/" + page.path
        mask = code_mask(page.body)
        for i, raw in enumerate(page.body):
            if mask[i]:
                continue
            raw = LINK_FULL.sub(
                lambda m: m.group(1) if m.group(2) in DEAD_ANCHORS else m.group(0), raw)

            def repl(m: re.Match) -> str:
                nonlocal fixed
                target = m.group(1)
                hit = index.get(target)
                if hit is None:
                    broken.append((page.path, target))
                    return m.group(0)
                dest, frag = hit
                fixed += 1
                if frag is None:
                    return f"]({dest})"
                if dest == route:
                    return f"](#{frag})"
                return f"]({dest}#{frag})"

            page.body[i] = LINK.sub(repl, raw)
    return fixed, broken


# --------------------------------------------------------------------------
# Emit
# --------------------------------------------------------------------------

def yaml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def write_pages(pages: list[Page]) -> None:
    for page in pages:
        dest = DOCS / f"{page.path}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        fm = ["---", f'title: "{yaml_escape(page.title)}"',
              f"sidebar_position: {page.position}"]
        if page.slug:
            fm.append(f"slug: {page.slug}")
        fm += ["---", ""]
        body = "".join(page.body).strip("\n")
        dest.write_text("\n".join(fm) + "\n" + body + "\n", encoding="utf-8")


def write_categories(chapters: list[Chapter]) -> None:
    labels = dict(CATEGORY_LABEL)
    for ch in chapters:
        if ch.category:
            labels[ch.out] = ch.category
    for folder, label in labels.items():
        d = DOCS / folder
        if not d.exists():
            continue
        (d / "_category_.json").write_text(json.dumps({
            "label": label,
            "position": CATEGORY_POSITION.get(folder, 99),
            "link": {"type": "generated-index", "title": label},
        }, indent=2) + "\n", encoding="utf-8")


def write_redirects(index: dict[str, tuple[str, str | None]], pages: list[Page]) -> None:
    by_route = {"/" + p.path: p for p in pages}
    mapping: dict[str, str] = {}
    for anchor, (route, frag) in sorted(index.items()):
        page = by_route.get(route)
        if page is None:
            continue
        target = page.slug or route
        mapping[anchor] = target if frag is None else f"{'' if target == '/' else target}#{frag}"
    (ROOT / "static" / "legacy-redirects.json").write_text(
        json.dumps(mapping, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"  legacy-redirects.json: {len(mapping)} hash targets")


def copy_images() -> None:
    """Mirror the Slate image folder into static/img/.

    Every file is copied, including the handful Slate itself never referenced,
    so nothing the team may still want is silently dropped.
    """
    src = SLATE / "images"
    IMG.mkdir(parents=True, exist_ok=True)
    n = 0
    for p in sorted(src.glob("*")):
        if p.is_file():
            shutil.copy2(p, IMG / p.name)
            n += 1
    print(f"  images: {n} copied to static/img/")


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main() -> int:
    if not INCLUDES.exists():
        print(f"!! Slate sources not found at {INCLUDES}", file=sys.stderr)
        return 1

    for stale in ("tutorial-basics", "tutorial-extras"):
        shutil.rmtree(DOCS / stale, ignore_errors=True)
    for stale in DOCS.glob("intro.*"):
        stale.unlink()
    for ch in PAGE_PLAN:
        shutil.rmtree(DOCS / ch.out, ignore_errors=True)
        for ext in (".md", ".mdx"):
            f = DOCS / (ch.out + ext)
            if f.exists():
                f.unlink()

    all_pages: list[Page] = []
    print("Reading Slate sources…")
    for ch in PAGE_PLAN:
        raw = (INCLUDES / f"{ch.src}.md").read_text(encoding="utf-8").splitlines(keepends=True)
        lines = mdx_safety(normalise_headings(raw))
        pages = split_chapter(ch, lines)
        all_pages.extend(pages)
        print(f"  {ch.src + '.md':22} -> {len(pages):2} page(s)")

    print(f"\nTotal: {len(all_pages)} pages")

    index = build_anchor_index(all_pages)
    print(f"Anchor index: {len(index)} ids")

    fixed, broken = rewrite_links(all_pages, index)
    print(f"Links rewritten: {fixed}")
    if broken:
        print(f"!! {len(broken)} unresolved anchors:")
        for page, target in sorted(set(broken)):
            print(f"     {page:38} -> #{target}")

    write_pages(all_pages)
    write_categories(PAGE_PLAN)
    copy_images()
    write_redirects(index, all_pages)
    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
