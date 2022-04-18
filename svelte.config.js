import preprocess from 'svelte-preprocess';
import { windi } from 'svelte-windicss-preprocess';
import cloudflare from '@sveltejs/adapter-cloudflare';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: [
		windi({}),
		preprocess(),
	],
	kit: {
		vite: { optimizeDeps: { include: ['lodash.get', 'lodash.isequal', 'lodash.clonedeep'] } },
		adapter: cloudflare(),
	}
};

export default config;
