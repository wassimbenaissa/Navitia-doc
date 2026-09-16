import type {PrismTheme} from 'prism-react-renderer';

/**
 * Syntax colours drawn from the HOVE palette.
 *
 * The stock github/dracula pair is the one place the design system could not
 * reach through CSS variables: prism-react-renderer writes the token colours as
 * inline styles. Six roles, six hues, all from `hove-tokens.css`:
 * ink/plain, warm brown for comments, brand cyan for keywords, blue teal for
 * functions, orange for strings, and the UI blue for numbers.
 */

const light: PrismTheme = {
  plain: {
    color: '#002830', // --dark-blue
    backgroundColor: '#f5f4f2', // --lightgrey-25
  },
  styles: [
    {
      types: ['comment', 'prolog', 'doctype', 'cdata'],
      style: {color: '#7c7369', fontStyle: 'italic'}, // --brown-90
    },
    {
      types: ['punctuation', 'operator', 'entity'],
      style: {color: '#405e64'}, // --darkblue-75
    },
    {
      types: ['keyword', 'tag', 'selector', 'rule', 'important', 'atrule'],
      style: {color: '#00758b'}, // brand cyan, text-safe step
    },
    {
      types: ['function', 'class-name', 'function-variable'],
      style: {color: '#004650'}, // --blue-teal
    },
    {
      types: ['string', 'char', 'attr-value', 'regex', 'url', 'inserted'],
      style: {color: '#b33800'}, // --orange, darkened for AA on light
    },
    {
      types: ['number', 'boolean', 'constant', 'symbol'],
      style: {color: '#0f4fc4'}, // --blue-ui, darkened
    },
    {
      types: ['property', 'attr-name', 'variable'],
      style: {color: '#00546a'},
    },
    {
      types: ['deleted'],
      style: {color: '#a8161e'}, // --error
    },
    {
      types: ['namespace'],
      style: {opacity: 0.7},
    },
  ],
};

const dark: PrismTheme = {
  plain: {
    color: '#e5eced', // --blueteal-10
    backgroundColor: '#001d23', // --darkblue-deep
  },
  styles: [
    {
      types: ['comment', 'prolog', 'doctype', 'cdata'],
      style: {color: '#80a2a7', fontStyle: 'italic'}, // --blueteal-50
    },
    {
      types: ['punctuation', 'operator', 'entity'],
      style: {color: '#bfd1d3'}, // --blueteal-25
    },
    {
      types: ['keyword', 'tag', 'selector', 'rule', 'important', 'atrule'],
      style: {color: '#40c2da'}, // --bluekeolis-75
    },
    {
      types: ['function', 'class-name', 'function-variable'],
      style: {color: '#bfebf3'}, // --bluekeolis-25
    },
    {
      types: ['string', 'char', 'attr-value', 'regex', 'url', 'inserted'],
      style: {color: '#fea381'}, // --orange-50
    },
    {
      types: ['number', 'boolean', 'constant', 'symbol'],
      style: {color: '#ffa144'}, // --warning
    },
    {
      types: ['property', 'attr-name', 'variable'],
      style: {color: '#00aece'}, // --blue-keolis
    },
    {
      types: ['deleted'],
      style: {color: '#ff9ea3'},
    },
    {
      types: ['namespace'],
      style: {opacity: 0.7},
    },
  ],
};

export const hovePrismThemes = {light, dark};
