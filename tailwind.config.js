/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
   './templates/**/*.html',   // Ensure your templates are included
    './static/**/*.js',        // Include JavaScript files if applicable
    './static/**/*.css',       // Include your CSS files if needed
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}