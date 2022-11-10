<script>
	import { active } from '$lib/store/store';

	let toggle = () => {
		active.update((val) => !val);
	};
</script>

<svelte:head>
	<title>CONCEPTION CALCULATOR 2000</title>
</svelte:head>

<section>
	<p href="/" class="centreButton alt" on:click={() => toggle()}>conception calculator 2000</p>
	<p class="hint">use arrow keys to swim</p>
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
