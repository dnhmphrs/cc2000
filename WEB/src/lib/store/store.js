import { writable } from 'svelte/store';

export const active = writable(false);
export const screenType = writable(3);
export const iframe = writable(null);

export const spicy = writable(5);
export const date = writable(null);
export const page = writable(1);
