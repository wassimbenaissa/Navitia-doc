import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import {hovePrismThemes} from './src/prism/hovePrismTheme';

const config: Config = {
  title: 'Navitia.io documentation',
  tagline: 'The open API for building cool stuff with mobility data',
  favicon: 'img/favicon.ico',

  // Defaults target GitHub Pages for this repo. Override both when deploying
  // behind the custom domain (SITE_URL=https://doc.navitia.io SITE_BASE_URL=/).
  url: process.env.SITE_URL ?? 'https://wassimbenaissa.github.io',
  baseUrl: process.env.SITE_BASE_URL ?? '/Navitia-doc/',
  organizationName: 'wassimbenaissa',
  projectName: 'Navitia-doc',
  trailingSlash: false,

  // The migration resolved every in-page anchor into a cross-page link.
  // Keep these strict so a bad link fails CI instead of shipping.
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',

  markdown: {
    hooks: {onBrokenMarkdownLinks: 'warn'},
  },

  i18n: {defaultLocale: 'en', locales: ['en']},

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
        },
        blog: false,
        // Design-system foundations first, then the Infima mapping that uses them.
        theme: {customCss: ['./src/css/hove-tokens.css', './src/css/custom.css']},
      } satisfies Preset.Options,
    ],
  ],

  // Inter (UI) + DM Mono (system/doc labels) — the two families the design
  // system takes from Google Fonts. Uxum Grotesque ships in static/fonts.
  headTags: [
    {
      tagName: 'link',
      attributes: {rel: 'preconnect', href: 'https://fonts.googleapis.com'},
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: 'anonymous',
      },
    },
  ],
  stylesheets: [
    'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap',
  ],

  themes: [
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {hashed: true, indexBlog: false, docsRouteBasePath: '/'},
    ],
  ],

  // Maps old single-page hashes (doc.navitia.io/#journeys) onto the new routes.
  // Fragments never reach the server, so this has to run in the browser.
  clientModules: ['./src/clientModules/legacyHashRedirect.ts'],

  themeConfig: {
    navbar: {
      title: 'Navitia.io',
      logo: {alt: 'Navitia', src: 'img/logo.png'},
      items: [
        {type: 'docSidebar', sidebarId: 'docs', position: 'left', label: 'Documentation'},
        {href: 'https://playground.navitia.io', label: 'Playground', position: 'right'},
        {href: 'https://github.com/hove-io/navitia', label: 'GitHub', position: 'right'},
      ],
    },
    footer: {
      style: 'dark',
      logo: {
        alt: 'HOVE',
        src: 'img/hove/hove-logo-cyan.png',
        href: 'https://www.hove.com',
        height: 28,
      },
      links: [
        {
          title: 'Navitia',
          items: [
            {label: 'Get an access', href: 'https://www.hove.com/fr/contact/'},
            {label: 'navitia.io', href: 'https://navitia.io'},
            {label: 'Navitia Playground', href: 'https://playground.navitia.io'},
            {label: 'Navitia on GitHub', href: 'https://github.com/hove-io/navitia'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Hove.`,
    },
    prism: {
      theme: hovePrismThemes.light,
      darkTheme: hovePrismThemes.dark,
      additionalLanguages: ['bash', 'json'],
    },
    colorMode: {respectPrefersColorScheme: true},
    docs: {
      sidebar: {hideable: true, autoCollapseCategories: false},
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
