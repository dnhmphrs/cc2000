<script>
	import { page } from '$lib/store/store';
	import { goto } from '$app/navigation';

	let handleProgress = () => {
		page.set(1);
		goto('/', { replaceState: true });
	};
</script>

<svelte:head>
	<title>CC2000 | System Meltdown</title>
	<!-- <link rel="preload" href="/gifs/the-future.gif" as="image/gif" /> -->
</svelte:head>
<section>
	<!-- <img src="/gifs/the-future.gif" alt="404 error" /> -->
	<h1 on:click={() => handleProgress()}>
		Short: Our servers overheated. The algorithm found your moment of conception too hot for
		calculation. Your parents FUCK.
	</h1>
</section>

<style>
	section {
		width: 100%;
		height: 100%;
		display: flex;
	}

	h1 {
		text-align: center;

		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		background: black;
		padding: 0.5rem 1rem;

		border: solid 1px var(--white-50);
		color: var(--white-50);

		cursor: pointer;
	}

	h1:hover {
		border-color: var(--white);
		color: var(--white);
	}
</style>
