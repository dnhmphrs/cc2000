<script>
	import { onMount, onDestroy } from 'svelte';
	import { go } from '$lib/store/store';
	// import { FlyControls } from 'three/examples/jsm/controls/FlyControls';
	import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
	import * as THREE from 'three';

	let container, pc, id;
	onDestroy(() => cancelAnimationFrame(id));

	// Setting up the scene
	let scene = new THREE.Scene();

	let height = window.innerHeight;
	let width = window.innerWidth;

	// Setting up a camera
	let camera = new THREE.PerspectiveCamera(25, width / height, 0.5, 400);
	camera.position.z = 160;

	let sperm;

	let firstLoad = true;

	// Setting up the renderer. This will be called later to render scene with the camera setup above
	let renderer = new THREE.WebGLRenderer({ antialias: false });
	renderer.setPixelRatio(window.devicePixelRatio);
	renderer.setSize(width, height);
	renderer.setClearColor(0x0033bb, 1);
	onMount(() => {
		container.appendChild(renderer.domElement);

		setTimeout(() => {
			window.dispatchEvent(new KeyboardEvent('keydown', { key: 's' }));
		}, '1000');
	});

	// let flyControls = new FlyControls(camera, renderer.domElement);
	// flyControls.dragToLook = true;
	// flyControls.movementSpeed = 100;
	// flyControls.rollSpeed = 0.05;
	// flyControls.autoForward = true;
	// flyControls.update(0.001);

	{
		const color = 0x0033bb;
		const density = 0.015;
		scene.fog = new THREE.FogExp2(color, density);
	}

	// ---------------------------------------------------------------------------

	const sphere = new THREE.Mesh(
		new THREE.SphereGeometry(7, 32, 16),
		new THREE.MeshToonMaterial({ color: 0xffc0cb })
	);
	scene.add(sphere);

	sphere.position.z += 2.5;

	const outerSphere = new THREE.Mesh(
		new THREE.SphereGeometry(11, 32, 16),
		// new THREE.MeshPhysicalMaterial({ roughness: 0.2, transmission: 0.8 })
		new THREE.MeshToonMaterial({ color: 0xffc0cb, transparent: true, opacity: 0.5 })
	);
	scene.add(outerSphere);

	const light = new THREE.HemisphereLight(0xf9d6ff, 0x0033bb, 2);
	scene.add(light);

	// ---------------------------------------------------------------------------

	const gltfLoader = new GLTFLoader();

	let spermGroup = new THREE.Group();
	gltfLoader.load('/sperm.glb', (glb) => {
		sperm = glb.scene.children[0];

		// sperm.position.z = 100;
		sperm.rotation.x += Math.PI;
		sperm.position.y -= 0.695;
		sperm.position.z += 4;

		sperm.scale.set(0.2, 0.4, 0.2);

		spermGroup.add(sperm);
	});

	scene.add(spermGroup);
	spermGroup.position.y = -0.1;

	// ---------------------------------------------------------------------------

	let followCamera = () => {
		spermGroup.position.z = camera.position.z;
	};

	let render = function () {
		renderer.render(scene, camera);
		id = requestAnimationFrame(render);
		// flyControls.update(0.001);

		if ($go) {
			camera.position.z -= 0.1;
		}

		if (camera.position.z <= 10) {
			renderer.setClearColor(0x000000, 1);
		}

		if (camera.position.z <= -10) {
			renderer.setClearColor(0x0033bb, 1);
			camera.position.z = 160;
			camera.position.y = 0;
			camera.position.x = 0;

			camera.lookAt(0, 0, 0);
		}

		spermGroup.rotation.z -= 0.15;
		// spermGroup.rotation.z -= (-spermGroup.rotation.z / Math.PI / 24 + 0.2) / 1.2;
		// if (spermGroup.rotation.z <= -2 * Math.PI) {
		// 	spermGroup.rotation.z = 0;
		// }

		followCamera();
		spermGroup.position.z -= 5.5;

		// spermGroup.position.z -= 3;

		if (firstLoad && camera.position.z >= 130) {
			camera.fov = 160 - camera.position.z;
			camera.updateProjectionMatrix();
		} else {
			firstLoad = false;
		}

		// this block fixes a bug where the sperm is brielfy visible after entering the
		// if (camera.position.z <= 10.5) {
		// 	spermGroup.position.z = -160;
		// }
	};

	window.addEventListener(
		'resize',
		function () {
			let height = window.innerHeight;
			let width = window.innerWidth;
			camera.aspect = width / height;
			camera.updateProjectionMatrix();
			renderer.setSize(width, height);
		},
		false
	);

	render();
</script>

<div bind:this={container} class:geometry={true} />

<style>
	.geometry {
		position: absolute;
		top: 0;
		left: 0;
		z-index: -10;
		overflow: hidden;

		width: 100vw;
		height: 100vh;
		height: calc(var(--vh, 1vh) * 100);
	}
</style>
