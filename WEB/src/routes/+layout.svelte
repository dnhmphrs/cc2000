<script>
	import '../app.css';
	import { onMount } from 'svelte';
	import { screenType, iframe } from '$lib/store/store';

	let Geometry;
	onMount(async () => {
		// ---------------------------------------------------------------------------
		// HEIGHT
		// ---------------------------------------------------------------------------

		// First we get the viewport height and we multiple it by 1% to get a value for a vh unit
		let vh = window.innerHeight * 0.01;
		// Then we set the value in the --vh custom property to the root of the document
		document.documentElement.style.setProperty('--vh', `${vh}px`);

		window.addEventListener('resize', () => {
			// We execute the same script as before
			let vh = window.innerHeight * 0.01;
			document.documentElement.style.setProperty('--vh', `${vh}px`);
		});

		const module = await import('./geometry.svelte');
		Geometry = module.default;

		// ---------------------------------------------------------------------------
		// SCREEN
		// ---------------------------------------------------------------------------
		const ua = navigator.userAgent;
		if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {
			// tablet
			screenType.set(1);
		} else if (
			/Mobile|Android|iP(hone|od)|IEMobile|BlackBerry|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(
				ua
			)
		) {
			// phone
			screenType.set(2);
		} else {
			//laptop
			screenType.set(3);
		}

		if (window.location !== window.parent.location) {
			// The page is in an iframe
			iframe.set(true);
		}
	});
</script>

<svelte:component this={Geometry} />

<main>
	<slot />
</main>

<style>
	main {
		height: 100vh;
		height: calc(var(--vh, 1vh) * 100);
		width: 100%;

		display: flex;
		align-items: center;
		justify-content: center;
	}
</style>
