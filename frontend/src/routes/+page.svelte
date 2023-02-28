<script lang="ts">
    import axios from 'axios';

	let data: any;
    async function test() {
		try {
			const response = await axios.get(window.location.origin + '/api/');
			data = response.data.detail;
		} catch (error: any) {
            console.log(error);
		}
	}
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<button on:click={async () => test()}>click me</button>
<p>{data}</p>
