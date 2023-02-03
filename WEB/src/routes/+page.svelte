<script>
	import { spicy } from '$lib/store/store';

	let handleGo = () => {
		go.set(true);
	};
</script>

<svelte:head>
	<title>CONCEPTION CALCULATOR 2000</title>
</svelte:head>

<section>
	<h6>CONCEPTION CALCULATOR 2000</h6>
	<!-- <div>

		<h1>CALCULATE THE SONG YOU WERE CONCEIVED TO</h1>
	</div>

	<div class="body">
		<div class="dob">
			<h5>DATE OF BIRTH</h5>
			<input type="date" />
		</div>

		<div class="spicy">
			<h5>HOW SPICY?</h5>
			<input type="range" id="volume" name="volume" min="0" max="10" />
		</div>
	</div>

	<div class="calculate" on:click={() => handleGo()}>
		<h5>CALCULATE</h5>
	</div> -->
</section>

<style>
	section {
		height: 100%;
		width: 100%;
		display: flex;
		overflow: auto;
		background: var(--blue);

		display: flex;
		flex-flow: column nowrap;
		align-items: center;

		justify-content: space-around;
		padding: 40px;
		margin: 20px;

		max-height: 540px;
		max-width: 540px;
		min-height: 540px;
		min-width: 540px;

		border: solid 4px var(--white);
	}

	.body {
		width: 100%;
		display: flex;
		flex-flow: row wrap;
		justify-content: space-between;
		padding: 10px 0;
		/* background: var(--white); */
		border: solid 4px var(--white);
	}

	.body div {
		width: 50%;
		display: flex;
		flex-flow: column wrap;
		align-items: center;
		gap: 10px;
		padding: 20px;
	}

	input {
		color: black;
		padding: 12px;
	}

	h1,
	h5 {
		font-family: 'degular-display', sans-serif;
		font-weight: 800;
		text-align: center;
	}

	h1 {
		font-size: 32px;
		letter-spacing: 2px;
	}

	h5 {
		font-size: 24px;
		padding-bottom: 0px;
		letter-spacing: 1px;
	}

	h6 {
		font-family: 'degular', sans-serif;
		font-weight: 500;
		font-size: 18px;

		text-align: center;
		letter-spacing: 4px;
		/* opacity: 0.25; */
		padding-bottom: 10px;
	}

	.calculate {
		width: 100%;
		height: 100px;
		/* background: var(--blue); */
		border: solid 4px var(--white);

		display: flex;
		align-items: center;
		justify-content: center;

		cursor: pointer;
	}

	.calculate h5 {
		padding-bottom: 0;
	}

	.calculate:hover {
		background: var(--white);
		color: var(--blue);
		border-color: var(--white);
	}

	.hint {
		align-self: flex-end;
		padding: 16px;
	}
</style>
