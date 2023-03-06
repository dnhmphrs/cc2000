<script>
	import { page } from '$lib/store/store';

	let handleProgress = () => {
		page.set(4);
	};
</script>

<section>
	<h1 on:click={() => handleProgress()}>Transitioning. Blah. Blah.</h1>
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
