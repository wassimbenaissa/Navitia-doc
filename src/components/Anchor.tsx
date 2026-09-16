import React from 'react';
import useBrokenLinks from '@docusaurus/useBrokenLinks';

/**
 * An inline link target that is not a heading.
 *
 * Slate allowed `<a name="traveler-type">` anywhere, including inside a table
 * cell, and the migration preserves those targets. A raw `<span id>` would
 * still work in the browser, but Docusaurus only knows about anchors that a
 * component registers, so `onBrokenAnchors: 'throw'` would flag every link to
 * one as broken. Registering here keeps that check meaningful.
 */
export default function Anchor({id}: {id: string}): React.ReactElement {
  useBrokenLinks().collectAnchor(id);
  return <span id={id} />;
}
