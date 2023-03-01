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
				<img src="/del.svg" class="h-8 w-auto mx-auto" alt="Delete" />
			</button>
		</div>
	</div>
</div>
