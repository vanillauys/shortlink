/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {},
		fontFamily: {
			'sans': ['Urbanist', 'system-ui'],
		}
	},
	plugins: [require('daisyui')],
	daisyui: {
		themes: ['dracula'],
	},
};
