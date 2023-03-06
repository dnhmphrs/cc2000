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
		height: 100%;
		display: flex;
	}

	h1 {
		text-align: center;

		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		/* background: black; */
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
