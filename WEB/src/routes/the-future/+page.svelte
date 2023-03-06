<script>
	let handleProgress = () => {
		page.set(1);
	};
</script>

<svelte:head>
	<title>CC2000 | 404</title>
</svelte:head>
<section>
	<img src="/gifs/the-future.gif" alt="404 error" />
	<h1 on:click={() => handleProgress()}>
		COPY: You were born in the After Time. Those lucky enough to be born were conceived to “Baby” by
		Justin Bieber as it is the only remaining music allowed by The Council.
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
