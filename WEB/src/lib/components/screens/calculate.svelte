<script>
	import { spicy, page, date } from '$lib/store/store';

	let handleProgress = () => {
		console.log($date);
		console.log($spicy);
		page.set(3);
	};
</script>

<section>
	<div>
		<h5>CONCEPTION CALCULATOR 2000</h5>
	</div>

	<div class="dob">
		<h6>DATE OF BIRTH</h6>
		<input type="date" bind:value={$date} />
	</div>

	<div class="spicy">
		<h6>HOW SPICY?</h6>
		<input type="range" id="volume" name="volume" bind:value={$spicy} min="0" max="10" />
	</div>

	<div class="calculate" on:click={() => handleProgress()}>
		<h6>CALCULATE</h6>
	</div>
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
		color: var(--white);
		padding: 1rem;
	}

	input[type='date'] {
		color: var(--black);
	}

	.calculate {
		border: solid 1px var(--white-50);
		color: var(--white-50);
		padding: 0.5rem 1rem;

		cursor: pointer;
	}

	.calculate:hover {
		border-color: var(--white);
		color: var(--white);
	}
</style>
