<script lang="ts">
    export let title: string;
    export let date: string;
    export let fullLink: string;
    export let shortLink: string;
</script>

<div class="collapse collapse-arrow border border-base-300 bg-neutral rounded-box">
	<input type="checkbox" />
	<div class="collapse-title text-xl font-medium">{shortLink}</div>
	<div class="collapse-content">
        <ul>
            <li>Title: {title}</li>
            <li>Full link: {fullLink}</li>
            <li>Date: {date}</li>
        </ul>
	</div>
</div>
