// Compile every generated doc with the MDX compiler to collect ALL syntax
// errors in one pass, instead of one-per-build-run.
import {compile} from '@mdx-js/mdx';
import {readFileSync} from 'node:fs';
import {globSync} from 'node:fs';
import {readdirSync, statSync} from 'node:fs';
import {join} from 'node:path';

function walk(dir) {
  return readdirSync(dir).flatMap((f) => {
    const p = join(dir, f);
    return statSync(p).isDirectory() ? walk(p) : p.endsWith('.md') ? [p] : [];
  });
}

const files = walk('docs');
let bad = 0;
for (const f of files) {
  // {#custom-id} heading anchors are a Docusaurus remark feature, not MDX.
  const src = readFileSync(f, 'utf8').replace(/\{#[\w.:-]+\}/g, '');
  try {
    await compile(src, {jsx: true});
  } catch (e) {
    bad++;
    const line = e.line ?? e.place?.start?.line ?? '?';
    const col = e.column ?? e.place?.start?.column ?? '?';
    const text = src.split('\n')[line - 1] ?? '';
    console.log(`${f}:${line}:${col}  ${e.reason ?? e.message}`);
    console.log(`    | ${text.slice(0, 160)}`);
  }
}
console.log(`\n${bad}/${files.length} files fail MDX compilation`);
