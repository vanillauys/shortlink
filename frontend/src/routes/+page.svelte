<script lang="ts">
	import axios from 'axios';
	import Link from '../lib/Link.svelte';
	import Error from '../lib/Error.svelte';
	import { onMount } from 'svelte';

	let url: string;
	let links: any;
	let loading: boolean = false;
	let errMsg: string;
	let error: boolean = false;

	async function shorten() {
		let data: any;
		loading = true;
		try {
			const response = await axios.post(window.location.origin + '/api/shorten', {
				url: url
			});
			data = response.data;
			await create_link(data);
			await get_all_links();
			error = false;
			errMsg = '';
			url = '';
			loading = false;
		} catch (e: any) {
			error = true;
			data = null;
			errMsg = e.response.data.detail;
			if (errMsg == undefined) {
				errMsg = 'Something went wrong...';
			}
			loading = false;
		}
	}

	async function create_link(link: any) {
		loading = true;
		let data: any;
		try {
			const response = await axios.post(window.location.origin + '/api/create', {
				status: link.status,
				fullLink: link.fullLink,
				date: link.date,
				shortLink: link.shortLink,
				title: link.title
			});
			data = response.data;
			error = false;
			errMsg = '';
			loading = false;
		} catch (e: any) {
			error = true;
			data = null;
			errMsg = e.response.data.detail;
			if (errMsg == undefined) {
				errMsg = 'Something went wrong...';
			}
			loading = false;
		}
	}

	async function delete_link(key: string) {
		loading = true;
		let data: any;
		try {
			const response = await axios.delete(window.location.origin + '/api/delete?key=' + key);
			data = response.data.detail;
			error = false;
			errMsg = '';
			loading = false;
			await get_all_links();
		} catch (e: any) {
			error = true;
			data = null;
			errMsg = e.response.data.detail;
			if (errMsg == undefined) {
				errMsg = 'Something went wrong...';
			}
			loading = false;
		}
	}

	async function get_all_links() {
		loading = true;
		try {
			const response = await axios.get(window.location.origin + '/api/get');
			links = response.data;
			error = false;
			errMsg = '';
			loading = false;
		} catch (e: any) {
			error = true;
			errMsg = e.response.data.detail;
			if (errMsg == undefined) {
				errMsg = 'Something went wrong...';
			}
			loading = false;
		}
	}

	onMount(async () => await get_all_links());
</script>

<div class="container px-12 py-12 flex flex-col justify-center mx-auto">
	<h1 class="mx-auto text-5xl uppercase font-thin tracking-wide">Shrtn</h1>
	<p class="text-xl mx-auto mt-6 font-normal">
		Simple URL shortener built on
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
		<Error {errMsg} />
	{/if}
</div>

<div class="container mx-auto py-12 px-12">
	{#if !loading && links != null && links.length > 0}
		{#each links as link}
			<Link
				title={link.title}
				fullLink={link.fullLink}
				shortLink={link.shortLink}
				date={link.date}
				key={link.key}
				{delete_link}
			/>
		{/each}
	{:else if loading}
		<div class="mx-auto w-2/5 my-12">
			<progress class="progress w-full mx-auto" />
		</div>
	{:else}
		<p class="py-12 mx-auto text-center">No links shortened yet...</p>
	{/if}
</div>
