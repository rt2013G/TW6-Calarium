import * as THREE from 'three';

/*
 * RENDERER
 */
const size = {
    width: window.innerWidth,
    height: window.innerHeight
}
const canvas = document.querySelector('.three-background');
const renderer = new THREE.WebGLRenderer({
    canvas: canvas
});
renderer.setSize( size.width, size.height );
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

/*
 * SCENE
 */
const scene = new THREE.Scene();
//scene.background = new THREE.Color( 0x2c2c33 );

/*
 * CAMERA
 */
const camera = new THREE.PerspectiveCamera(90, size.width / size.height, 0.1, 1000);
camera.position.setX(0);
camera.position.setZ(0);
scene.add(camera);

/*
 * LIGHTING
 */
const pointLight = new THREE.PointLight(0xffffff);
pointLight.position.set(5, 5, 5);

const ambientLight = new THREE.AmbientLight(0xffffff);
scene.add(pointLight, ambientLight);

/*
 * OBJECTS
 */
function generateStaticStars(count, radius, color, distance) {
    Array(count).fill().forEach(() => {
        const starGeometry = new THREE.SphereGeometry(radius, 32, 16);
        const starMaterial = new THREE.MeshStandardMaterial({
            color: color
        });
        const starMesh = new THREE.Mesh(starGeometry, starMaterial);

        const [x, y, z] = Array(3)
            .fill()
            .map(() => THREE.MathUtils.randFloatSpread(100 + distance));

        starMesh.position.set(x, y, z);
        scene.add(starMesh);
    });
}
generateStaticStars(150, 0.1, 0xfff100, 200);
generateStaticStars(150, 0.16, 0xffffff, 300);
generateStaticStars(500, 0.2, 0xffffff, 750);
generateStaticStars(1000, 0.15, 0xffffff, 100);

const movingStarGeometry = new THREE.BufferGeometry;
const movingStarMaterial= new THREE.PointsMaterial({ size: 0.04 });
const movingStarsCount = 500;
const movingStarsPosition = new Float32Array(movingStarsCount * 3);

for(let i = 0; i < movingStarsCount * 3; i++) {
    movingStarsPosition[i] = (Math.random() - 0.5) * 30;
}
movingStarGeometry.setAttribute('position', new THREE.BufferAttribute(movingStarsPosition, 3));
const movingStarsMesh =  new THREE.Points(movingStarGeometry, movingStarMaterial);

scene.add(movingStarsMesh);


const moonTexture = new THREE.TextureLoader().load('static/assets/texture/moon.jpg');
const normalTexture = new THREE.TextureLoader().load('static/assets/texture//normal.jpg');

const moon = new THREE.Mesh(
    new THREE.SphereGeometry(10, 32, 32),
    new THREE.MeshStandardMaterial({
        map: moonTexture,
        normalMap: normalTexture,
    })
);
moon.position.z = -40;
moon.position.x = 50;
moon.position.y = 15;
scene.add(moon);

/*
 * LISTENERS
 */
window.addEventListener('resize', () => {
    size.width = window.innerWidth;
    size.height = window.innerHeight;
    camera.aspect = size.width / size.height;
    camera.updateProjectionMatrix();

    renderer.setSize(size.width, size.height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
})

let mouseX = 0;
let mouseY = 0;
document.addEventListener('mousemove', (event) => {
    mouseX = event.clientX;
    mouseY = event.clientY;
})

/*
 * MAIN FUNCTION
 */
const clock = new THREE.Clock()

function animate() {
    const deltaTime = clock.getElapsedTime()

    movingStarsMesh.rotation.x = -0.04 * deltaTime;
    movingStarsMesh.rotation.y = 0.05 * deltaTime;
    if(mouseX > 0) {
        movingStarsMesh.rotation.x = -mouseY * deltaTime * 0.00005;
        movingStarsMesh.rotation.y = mouseX * deltaTime * 0.0001;
    }
    moon.rotation.x -= 0.0008;
    moon.rotation.y += 0.0008;

    renderer.render( scene, camera );
    requestAnimationFrame( animate );
}

animate();
