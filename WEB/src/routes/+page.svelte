<script>
	import Start from '$lib/components/screens/start.svelte';
	import Input from '$lib/components/screens/input.svelte';
	import Transition from '$lib/components/screens/transition.svelte';
	import Output from '$lib/components/screens/output.svelte';

	import { page } from '$lib/store/store';
</script>

<svelte:head>
	<title>CONCEPTION CALCULATOR 2000</title>
</svelte:head>

{#if $page == 1}
	<Start />
{:else if $page == 2}
	<Input />
{:else if $page == 3}
	<Transition />
{:else if $page == 4}
	<Output />
{/if}

<style>
</style>
