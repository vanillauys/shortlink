<script lang="ts">
	export let title: string;
	export let date: string;
	export let fullLink: string;
	export let shortLink: string;
</script>

<div class="collapse collapse-arrow border border-base-300 bg-neutral rounded-box">
	<input type="checkbox" />
	<div class="collapse-title text-xl font-medium">
        {title}
	</div>
	<div class="collapse-content">
		<ul class="text-lg justify-items-start flex flex-col">
			<li class="mx-auto">Short Link: 
                <a href="{shortLink}">{shortLink}</a>
            </li>
			<li class="mx-auto">Full link: 
                <a href="{fullLink}">{fullLink}</a>
            </li>
			<li class="mx-auto">Date: {date}</li>
		</ul>
	</div>
</div>
