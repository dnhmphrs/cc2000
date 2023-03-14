<script>
	import { onMount, onDestroy } from 'svelte';
	// import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
	import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
	import * as THREE from 'three';

	import AsciiRenderer from '$lib/components/effects/ascii-renderer.js';
	// console.log(AsciiRenderer);

	let container, pc, id;
	onDestroy(() => cancelAnimationFrame(id));

	// Setting up the scene
	let scene = new THREE.Scene();

	let height = window.innerHeight;
	let width = window.innerWidth;

	// Setting up a camera
	let camera = new THREE.PerspectiveCamera(30, width / height, 0.5, 400);
	camera.position.z = 100;

	let sperm, mac;

	var asciiRenderer;
	var charSet =
		'0100011001101111011100100010000001000111011011110' +
		'1100100001000000111001101101111001000000110110001' +
		'1011110111011001100101011001000010000001110100011' +
		'0100001100101001000000111011101101111011100100110' +
		'1100011001000010000001110100011010000110000101110' +
		'1000010000001101000011001010010000001100111011000' +
		'0101110110011001010010000001101000011010010111001' +
		'1001000000110111101101110011001010010000001100001' +
		'0110111001100100001000000110111101101110011011000' +
		'1111001001000000101001101101111011011100010110000' +
		'1000000111010001101000011000010111010000100000011' +
		'1011101101000011011110110010101110110011001010111' +
		'0010001000000110001001100101011011000110100101100' +
		'1010111011001100101011100110010000001101001011011' +
		'1000100000011010000110100101101101001000000111001' +
		'1011010000110000101101100011011000010000001101110' +
		'0110111101110100001000000111000001100101011100100' +
		'1101001011100110110100000100000011000100111010101' +
		'1101000010000001101000011000010111011001100101001' +
		'0000001100101011101000110010101110010011011100110' +
		'0001011011000010000001101100011010010110011001100' +
		'10100100000';

	// Setting up the renderer. This will be called later to render scene with the camera setup above
	let renderer = new THREE.WebGLRenderer({ antialias: false, alpha: true });
	renderer.setClearColor(0x232323, 1);

	// renderer.setPixelRatio(window.devicePixelRatio);
	// renderer.setSize(width, height);

	onMount(() => {
		container.appendChild(renderer.domElement);

		asciiRenderer = new AsciiRenderer(renderer, {
			charSet: charSet,
			fontSize: 4,
			opacity: 0.25
		});

		asciiRenderer.setSize(width, height);

		setTimeout(() => {
			window.dispatchEvent(new KeyboardEvent('keydown', { key: 's' }));
		}, '1000');
	});

	// let controls = new OrbitControls(camera, renderer.domElement);
	// controls.enablePan = false;
	// controls.enableZoom = false;
	// controls.minAzimuthAngle = -Math.PI / 4;
	// controls.maxAzimuthAngle = (Math.PI * 3) / 4;
	// controls.enableDamping = true;
	// controls.dampingFactor = 0.07;
	// controls.rotateSpeed = 0.05;
	// controls.update();

	{
		const color = 0x232323;
		const density = 0.009;
		scene.fog = new THREE.FogExp2(color, density);
	}

	// ---------------------------------------------------------------------------

	const size = 100;
	const divisions = 10;

	const gridHelper0 = new THREE.GridHelper(size, divisions, 0xf9d6ff, 0xf9d6ff);
	gridHelper0.rotation.x += Math.PI / 2;
	gridHelper0.position.z -= 300;
	scene.add(gridHelper0);

	const gridHelper1 = new THREE.GridHelper(size, divisions, 0xf9d6ff, 0xf9d6ff);
	gridHelper1.rotation.x += Math.PI / 2;
	gridHelper1.position.z -= 200;
	scene.add(gridHelper1);

	const gridHelper2 = new THREE.GridHelper(size, divisions, 0xf9d6ff, 0xf9d6ff);
	gridHelper2.rotation.x += Math.PI / 2;
	gridHelper2.position.z -= 100;
	scene.add(gridHelper2);

	const gridHelper3 = new THREE.GridHelper(size, divisions, 0xf9d6ff, 0xf9d6ff);
	gridHelper3.rotation.x += Math.PI / 2;
	gridHelper3.position.z -= 0;
	scene.add(gridHelper3);

	const sphere = new THREE.Mesh(
		new THREE.SphereGeometry(14, 32, 16),
		new THREE.MeshToonMaterial({ color: 0xffc0cb })
	);
	scene.add(sphere);

	const outerSphere = new THREE.Mesh(
		new THREE.SphereGeometry(22, 32, 16),
		// new THREE.MeshPhysicalMaterial({ roughness: 0.2, transmission: 0.8 })
		new THREE.MeshPhysicalMaterial({ color: 0xffc0cb, transparent: true, opacity: 0.5 })
	);
	scene.add(outerSphere);

	sphere.position.z = -150;
	outerSphere.position.z = -150;

	const light = new THREE.HemisphereLight(0xf9d6ff, 0x0033bb, 2.5);
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

	let macGroup = new THREE.Group();
	gltfLoader.load('/mac.glb', (glb) => {
		mac = glb.scene.children[0];

		// mac.traverse(function (child) {
		// 	if (child.material) {
		// 		child.material = new THREE.MeshPhongMaterial({
		// 			color: 0xd0d0d0,
		// 			wireframe: true,
		// 			vertexColors: THREE.VertexColors
		// 		});
		// 	}
		// });

		// macGroup.add(mac);
	});

	scene.add(macGroup);
	macGroup.position.z = 5;
	macGroup.position.z = -150;
	macGroup.position.y = -28;

	// ---------------------------------------------------------------------------

	let followCamera = () => {
		spermGroup.position.z = camera.position.z - 5.5;
	};

	const clock = new THREE.Clock();
	let previousTime = 0;

	let render = function () {
		renderer.render(scene, camera);
		id = requestAnimationFrame(render);
		// controls.update();

		const elapsedTime = clock.getElapsedTime();
		const deltaTime = elapsedTime - previousTime;
		previousTime = elapsedTime;

		//sphere.rotation.x += 0.01;
		// macGroup.position.z += 1;

		// if ($go) {
		// 	camera.position.z -= deltaTime * 20;
		// 	camera.rotation.z += deltaTime / 5;
		// }

		// camera.position.z -= deltaTime * 20;
		camera.position.z -= deltaTime * 12.725;
		gridHelper0.rotation.y -= deltaTime / 10;
		gridHelper1.rotation.y += deltaTime / 10;
		gridHelper2.rotation.y -= deltaTime / 10;
		gridHelper3.rotation.y += deltaTime / 10;

		// if (macGroup.rotation.y <= 0) {
		// 	macGroup.rotation.y += 0.003;
		// }

		// if (camera.position.z <= 10) {
		// 	renderer.setClearColor(0x000000, 1);
		// }

		if (camera.position.z <= -200) {
			camera.position.z = 100;
			// macGroup.rotation.y = -Math.PI;
		}

		spermGroup.rotation.z -= deltaTime * 10;

		// spermGroup.rotation.z -= (-spermGroup.rotation.z / Math.PI / 24 + 0.2) / 1.2;
		// if (spermGroup.rotation.z <= -2 * Math.PI) {
		// 	spermGroup.rotation.z = 0;
		// }

		followCamera();

		// if (firstLoad && camera.position.z >= 100) {
		// 	camera.fov = 160 - camera.position.z;
		// 	camera.updateProjectionMatrix();
		// } else {
		// 	firstLoad = false;
		// }

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
			// renderer.setSize(width, height);
			asciiRenderer.setSize(width, height);
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
