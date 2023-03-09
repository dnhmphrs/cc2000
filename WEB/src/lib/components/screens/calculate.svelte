<script>
	import { spicy, page, date, track } from '$lib/store/store';
	import { goto } from '$app/navigation';

	import data from '$lib/data/cc2000_data.json';

	let conceptionDate = (date_str) => {
		// get conception date
		let date = new Date(date_str);
		date.setDate(date.getDate() - 268);
		let dateString = date.toISOString().slice(0, 10);
		//console.log(dateString);

		return dateString;
	};

	let previousDay = (date_str) => {
		// get previous day
		let date = new Date(date_str);
		date.setDate(date.getDate() - 1);
		let dateString = date.toISOString().slice(0, 10);
		//console.log(dateString);

		return dateString;
	};

	let handleEdgeCases = (date) => {
		let error = false;

		let today = new Date();
		let todayString = today.toISOString().slice(0, 10);
		console.log(todayString);

		// if date is before 1958-06-01
		if (date <= '1958-06-01') {
			goto('/the-past', { replaceState: true });
			error = true;
		}
		// if date is after 2023-03-05
		if (date >= todayString) {
			goto('/the-future', { replaceState: true });
			error = true;
		}

		return error;
	};

	let handleProgress = () => {
		let conception_date = conceptionDate($date);
		let error = handleEdgeCases(conception_date);

		if (!error) {
			while (true) {
				try {
					track.set(data[conception_date][$spicy]);
					break;
				} catch (error) {
					conception_date = previousDay(conception_date);
				}
			}

			track.set(data[conception_date][$spicy]);
			console.log($track);
			page.set(3);
		}
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
		<input type="range" id="volume" name="volume" bind:value={$spicy} min="0" max="9" />
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
