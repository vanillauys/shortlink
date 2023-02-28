<script lang="ts">
	import axios from 'axios';

	let url: string;
	let data:any;

	async function shorten() {
		try {
			const response = await axios.post(window.location.origin + '/api/shorten', {
				url: url
			});
			data = response.data;
		} catch (error: any) {
			console.log(error);
		}
	}

</script>

<div class="container px-12 py-12 flex flex-col justify-center">
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
			<input type="submit" value="shorten it!" class="btn btn-secondary items-center font-normal lowercase" />
		</div>
	</form>
</div>

<div class="container">
	{data}
</div>
