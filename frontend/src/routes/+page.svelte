<script lang="ts">
	import axios from 'axios';
	import Link from '../lib/Link.svelte';
	import Error from '../lib/Error.svelte';

	let url: string;
	let data: any = null;
	let loading: boolean = false;
	let errMsg: string;
	let error: boolean = false;

	async function shorten() {
		loading = true;
		try {
			const response = await axios.post(window.location.origin + '/api/shorten', {
				url: url
			});
			data = response.data;
			error = false;
			errMsg = '';
			loading = false;
		} catch (e: any) {
			error = true;
			data = null;
			errMsg = e.response.data.detail;
			loading = false;
		}
	}
</script>

<div class="container px-12 py-12 flex flex-col justify-center mx-auto">
	<h1 class="mx-auto text-5xl uppercase font-thin tracking-wide">Shrtn</h1>
	<p class="text-xl mx-auto mt-6 font-normal">
		A simple URL shortener built on
		<a href="https://deta.space" target="_blank" rel="noreferrer" class="italic"> Deta.space 🚀 </a>
	</p>

	<form class="mx-auto w-4/5 max-w-2xl" on:submit|preventDefault={() => shorten()}>
		<input
			type="text"
			placeholder="https://deta.space/"
			class="input input-bordered input-info w-full mx-auto mt-12"
			required
			inputmode="url"
			bind:value={url}
		/>
		<div class="flex justify-center mt-8">
			<input
				type="submit"
				value="shorten it!"
				class="btn btn-secondary items-center font-normal lowercase"
			/>
		</div>
	</form>

	{#if error}
		<Error errMsg={errMsg} />
	{/if}

</div>

<div class="container mx-auto py-12 px-12">
	{#if !loading && data != null}	
		<Link title={data.title} fullLink={data.fullLink} shortLink={data.shortLink} date={data.date} />
	{:else if loading}
		<progress class="progress w-2/5 mx-auto py-12"></progress>
	{:else}
		<p class="py-12 mx-auto text-center">No links shortened yet...</p>
	{/if}
</div>
