<script>
	import { active } from '$lib/store/store';

	let toggle = () => {
		active.update((val) => !val);
	};
</script>

<svelte:head>
	<title>AUFBAU WEB STUDIO</title>
</svelte:head>

<section>
	<p href="/" class="centreButton alt" on:click={() => toggle()}>conception calculator 2000</p>
</section>

<style>
	section {
		height: 100%;
		display: flex;
		overflow: auto;
		max-width: 800px;
	}
</style>
