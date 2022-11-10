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
	<p class="centreButton alt">
		conception calculator 2000<br />coming soon
	</p>
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
