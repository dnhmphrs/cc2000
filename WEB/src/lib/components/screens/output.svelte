<script>
	import { page } from '$lib/store/store';

	let handleProgress = () => {
		page.set(1);
	};
</script>

<section>
	<iframe
		style="border-radius:12px"
		src="https://open.spotify.com/embed/track/6epn3r7S14KUqlReYr77hA?utm_source=generator"
		width="100%"
		height="352"
		frameBorder="0"
		allowfullscreen=""
		allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
		loading="lazy"
	/>
	<h1 on:click={() => handleProgress()}>Output. Whatevs.</h1>
</section>

<style>
	section {
		width: 100%;
		height: 50%;
		display: flex;
		flex-flow: column nowrap;

		justify-content: space-around;
		align-items: center;

		border: solid 1px var(--white-50);
		color: var(--white-50);
		padding: 1rem;
	}

	h1 {
		text-align: center;
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
