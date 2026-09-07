/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        bg: '#F7F4EF',
        ink: '#1B1B18',
        'ink-muted': '#6B6860',
        'ink-faint': '#9E9B93',
        accent: '#C1592B',
        terracotta: '#C1592B',
        'terracotta-hover': '#AB4B22',
        teal: '#1F3A3D',
        'teal-hover': '#162C2E',
        'teal-soft': '#EBF1F1',
        'accent-teal': '#1F3A3D',
        surface: '#FFFFFF',
        border: '#E6E1D8',
        grayBadge: '#68645C',
        grayBadgeBg: '#EFECE6',
      },
      fontFamily: {
        serif: ['Fraunces', 'Georgia', 'serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'ui-monospace', 'monospace'],
      },
      spacing: {
        'gutter-mobile': '1rem',
        'gutter-desktop': '2rem',
        'max-width-container': '1200px',
        'max-width-editorial': '720px',
      },
      maxWidth: {
        container: '1200px',
        editorial: '720px',
      },
      borderRadius: {
        sm: '0.125rem',
        DEFAULT: '0.25rem',
        md: '0.375rem',
        lg: '0.5rem',
        xl: '0.75rem',
        full: '9999px',
      },
      boxShadow: {
        editorial: '0 8px 24px -6px rgba(27, 27, 24, 0.07), 0 2px 6px -2px rgba(27, 27, 24, 0.04)',
        'editorial-hover': '0 12px 32px -6px rgba(27, 27, 24, 0.1), 0 4px 8px -2px rgba(193, 89, 43, 0.08)',
      },
    },
  },
  plugins: [],
};
