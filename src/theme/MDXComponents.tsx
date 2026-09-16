import type {ComponentProps} from 'react';
import MDXComponents from '@theme-original/MDXComponents';
import Anchor from '@site/src/components/Anchor';

// The reference tables are wide; give each one its own horizontal scroll
// container so a long cell can never spill over the right-hand TOC.
function Table(props: ComponentProps<'table'>) {
  return (
    <div className="tableWrapper">
      <table {...props} />
    </div>
  );
}

// Exposed to every .md page without an import.
export default {
  ...MDXComponents,
  table: Table,
  Anchor,
};
