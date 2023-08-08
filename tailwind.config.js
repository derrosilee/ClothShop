/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./accounts/templates/account/*.html'],
  theme: {
    extend: {},
  },
  plugins: [
      require('@tailwindcss/forms'),
  ],
}

