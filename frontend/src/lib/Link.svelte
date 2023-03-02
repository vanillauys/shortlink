<script lang="ts">
	export let title: string;
	export let date: string;
	export let fullLink: string;
	export let shortLink: string;
	export let key: string;
	export let delete_link: Function;
</script>

<div class="collapse collapse-arrow border border-base-300 bg-neutral rounded-box mt-4">
	<input type="checkbox" />
	<div class="collapse-title text-xl font-medium">
		{title}
	</div>
	<div class="collapse-content">
		<ul class="text-lg justify-center flex flex-col">
			<li class="mx-auto"><a href={shortLink} target="_blank" rel="noreferrer">{shortLink}</a></li>
			<li class="mx-auto"><a href={fullLink} target="_blank" rel="noreferrer">{fullLink}</a></li>
			<li class="mx-auto">{date}</li>
		</ul>
		<div class="flex justify-center">
			<button
				class="btn btn-error mt-4 w-10 mx-auto text-center"
				on:click={async () => await delete_link(key)}
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-14 w-14 text-xl mx-auto"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					><path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M6 18L18 6M6 6l12 12"
					/></svg
				>
			</button>
		</div>
	</div>
</div>
