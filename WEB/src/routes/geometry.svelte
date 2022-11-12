<script>
	import { onMount, onDestroy } from 'svelte';
	import { FlyControls } from 'three/examples/jsm/controls/FlyControls';
	import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
	import * as THREE from 'three';

	let container, pc, id;
	onDestroy(() => cancelAnimationFrame(id));

	// Setting up the scene
	let scene = new THREE.Scene();

	let height = window.innerHeight;
	let width = window.innerWidth;

	// Setting up a camera
	let camera = new THREE.PerspectiveCamera(25, width / height, 0.01, 400);
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
		}, '2000');
	});

	let flyControls = new FlyControls(camera, renderer.domElement);
	flyControls.dragToLook = true;
	flyControls.movementSpeed = 100;
	flyControls.rollSpeed = 0.05;
	flyControls.autoForward = true;
	flyControls.update(0.001);

	{
		const color = 0x0033bb;
		const density = 0.019;
		scene.fog = new THREE.FogExp2(color, density);
	}

	// ---------------------------------------------------------------------------

	const sphere = new THREE.Mesh(
		new THREE.SphereGeometry(10, 32, 16),
		new THREE.MeshToonMaterial({ color: 0xd0d0d0 })
	);
	scene.add(sphere);

	// const plane = new THREE.Mesh(
	// 	new THREE.PlaneGeometry(20, 20),
	// 	new THREE.MeshToonMaterial({ color: 0x000000 })
	// );
	// scene.add(plane);

	// const plane2 = new THREE.Mesh(
	// 	new THREE.PlaneGeometry(5, 5),
	// 	new THREE.MeshToonMaterial({ color: 0x000000 })
	// );
	// scene.add(plane2);
	// plane2.position.z -= 10;

	const light = new THREE.HemisphereLight(0xf9d6ff, 0x0033bb, 2);
	scene.add(light);

	// ---------------------------------------------------------------------------

	const gltfLoader = new GLTFLoader();

	let spermGroup = new THREE.Group();
	gltfLoader.load('/sperm.glb', (glb) => {
		sperm = glb.scene.children[0];

		sperm.scale.set(1, 1, 1);
		// sperm.position.z = 100;
		sperm.rotation.x += Math.PI;
		sperm.position.y -= 0.71;
		sperm.position.z += 4;

		sperm.scale.set(0.4, 0.4, 0.4);

		// sperm.material = material;

		// let bun2 = bun.clone();
		// bun2.material = new THREE.MeshBasicMaterial({
		// 	color: 0x141414,
		// 	wireframe: true
		// });
		// bun2.scale.set(8.03, 8.03, 8.03);

		spermGroup.add(sperm);
	});

	scene.add(spermGroup);

	// ---------------------------------------------------------------------------

	// Setting up a group to hold the items we will be creating together
	let group = new THREE.Group();

	// Array curve holds the positions of points generated from a lorenz equation; lorenz function below generates the points and returns an array of points
	let arrayCurve = lorenz();

	// Generating the geometry
	let curve = new THREE.CatmullRomCurve3(arrayCurve);
	let vertices = curve.getPoints(100000);
	let geometry = new THREE.BufferGeometry().setFromPoints(vertices);

	// Generating a cloud of point
	let pcMat = new THREE.PointsMaterial();
	pcMat.color = new THREE.Color(0x2053db);
	pcMat.transparent = true;
	pcMat.size = 0.1;
	// pcMat.blending = THREE.AdditiveBlending;
	pc = new THREE.Points(geometry, pcMat);
	pc.sizeAttenuation = true;
	pc.sortPoints = true;

	group.add(pc);

	scene.add(group);

	group.rotation.y += Math.PI / 2;

	let step = 0;

	let followCamera = () => {
		spermGroup.position.z = camera.position.z;
		spermGroup.position.x = camera.position.x;
		spermGroup.position.y = camera.position.y - 0.1;

		// spermGroup.rotation.z += camera.rotation.z;
		spermGroup.rotation.x = camera.rotation.x * 1.2;
		spermGroup.rotation.y = camera.rotation.y * 1.2;
	};

	let render = function () {
		renderer.render(scene, camera);
		id = requestAnimationFrame(render);
		flyControls.update(0.0013);

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

		spermGroup.rotation.z -= 0.125;

		followCamera();
		spermGroup.position.z -= 6;

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

		//Varying the points on each frame
		step += 0.000005;
		let geometry = pc.geometry;
		let a = 0.9 + Math.random() * 7;
		let b = 3.4 + Math.random() * 8;
		let f = 9.9 + Math.random() * 9;
		let g = 1 + Math.random();
		let t = 0.0005;

		// geometry.vertices.forEach(function (v) {
		// 	v.x = v.x - t * a * v.x + t * v.y * v.y - t * v.z * v.z + t * a * f;
		// 	v.y = v.y - t * v.y + t * v.x * v.y - t * b * v.x * v.z + t * g;
		// 	v.z = v.z - t * v.z + t * b * v.x * v.y + t * v.x * v.z;
		// });
		// geometry.verticesNeedUpdate = true;

		const positions = geometry.attributes.position.array;
		for (let i = 0; i < positions.length; i += 3) {
			let v = new THREE.Vector3(positions[i], positions[i + 1], positions[i + 2]);
			positions[i] = v.x - t * a * v.x + t * v.y * v.y - t * v.z * v.z + t * a * f;
			positions[i + 1] = v.y - t * v.y + t * v.x * v.y - t * b * v.x * v.z + t * g;
			positions[i + 2] = v.z - t * v.z + t * b * v.x * v.y + t * v.x * v.z;
		}

		geometry.attributes.position.needsUpdate = true;

		// group.rotation.x += 0.002;
		// group.rotation.y += 0.002;
		// group.rotation.z += 0.002;
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

	function lorenz() {
		let arrayCurve = [];

		let x = 0.01,
			y = 0.01,
			z = 0.01;
		let a = 4.9;
		let b = 5.4;
		let f = 7.9;
		let g = 1;
		let t = 0.000008;
		for (let i = 0; i < 100000; i++) {
			x = x - t * a * x + t * y * y - t * z * z + t * a * f;
			y = y - t * y + t * x * y - t * b * x * z + t * g;
			z = z - t * z + t * b * x * y + t * x * z;
			arrayCurve.push(new THREE.Vector3(x, y, z).multiplyScalar(2));
		}
		return arrayCurve;
	}
</script>

<div bind:this={container} class:geometry={true} />

<style>
	.geometry {
		position: fixed;
		top: 0;
		left: 0;
		z-index: -10;
		overflow: hidden;

		width: 100vw;
		height: 100vh;
		height: calc(var(--vh, 1vh) * 100);
	}
</style>
