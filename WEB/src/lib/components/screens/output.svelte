<script>
	import { page, track } from '$lib/store/store';

	let uri = $track.spotify_uri.substring(14);
	console.log(uri);
	let src = `https://open.spotify.com/embed/track/${uri}?utm_source=generator`;

	let handleProgress = () => {
		page.set(1);
	};
</script>

<section>
	<!-- svelte-ignore a11y-missing-attribute -->
	<iframe
		style="border-radius:12px"
		{src}
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

		background: var(--blue);
		color: var(--white);
		border: solid 1px var(--white);

		padding: 1rem;
	}

	h1 {
		text-align: center;
		padding: 0.5rem 1rem;
		background: black;
		border: solid 1px var(--white-50);
		color: var(--white-50);

		cursor: pointer;
	}

	h1:hover {
		border-color: var(--white);
		color: var(--white);
	}
</style>
