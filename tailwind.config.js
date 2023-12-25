/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{vue,js,ts}',   // Include all your Vue files in the pages directory
    './layouts/**/*.{vue,js,ts}',  // Include all your Vue files in the layouts directory
    './components/**/*.{vue,js,ts}', // Include all your Vue files in the components directory
    // You can add more paths here if you have other directories where you use Tailwind CSS
  ],
  theme: {
    extend: {
      // Here you can extend the default Tailwind theme
      // For example, you can add custom colors, spacing, fonts, etc.
    },
  },
  plugins: [
    // Here you can add any Tailwind CSS plugins you might be using
    // For example, 'require('@tailwindcss/forms')' if you're using the forms plugin
  ],
}
