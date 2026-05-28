import type { Config } from 'tailwindcss'

export default {
  content: [
    './frontend/components/**/*.{js,vue,ts}',
    './frontend/layouts/**/*.vue',
    './frontend/pages/**/*.vue',
    './frontend/plugins/**/*.{js,ts}',
    './frontend/app.vue',
  ],
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT: '#1E3A5F', light: '#2D5A8E', dark: '#142740' },
        secondary: { DEFAULT: '#F59E0B', light: '#FBBF24', dark: '#D97706' },
      },
    },
  },
} satisfies Config