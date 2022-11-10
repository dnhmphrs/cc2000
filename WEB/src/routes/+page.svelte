<script>
	import { screenType } from '$lib/store/store';
</script>

<svelte:head>
	<title>CONCEPTION CALCULATOR 2000</title>
</svelte:head>

<section>
	<p class="centreButton alt">conception calculator 2000 coming soon</p>
	{#if $screenType == 3}
		<p class="hint">use arrow keys to swim</p>
	{/if}
</section>

<style>
	section {
		height: 100%;
		display: flex;
		overflow: auto;
		max-width: 800px;
	}

	.hint {
		align-self: flex-end;
		padding: 16px;
	}
</style>
