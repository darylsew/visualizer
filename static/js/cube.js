var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, 700/500, 0.1, 1000)
//field of view, aspect ratio, minimum and maximum distances to render something
camera.position.z = 1.5;
var renderer = new THREE.WebGLRenderer(); // will go through render loop
renderer.setSize(700,500);
document.body.appendChild(renderer.domElement);

var geometry = new THREE.CubeGeometry(1,1,1);
var material = new THREE.MeshLambertMaterial({ color:0x00ff00 });
var cube = new THREE.Mesh(geometry, material);
scene.add(cube);

var planeGeometry = new THREE.PlaneGeometry(50,50,150,150);
var planeMaterial = new THREE.MeshPhongMaterial({ color:0xf0f0f0 });
var plane = new THREE.Mesh(planeGeometry, planeMaterial);
scene.add(plane);
plane.position.z = -21;

var pointlight = new THREE.PointLight(0xFFFFFF);
pointlight.position.z = 5;
scene.add(pointlight);

var index = 0; //beginning of the song
function render() {
    requestAnimationFrame(render);
    renderer.render(scene,camera);
    cube.material.color.setHex(fake_centroids[index]);
    index++;
    cube.rotation.x = Math.cos(index/50);
    cube.rotation.y = Math.sin(index/50);
    camera.lookAt(new THREE.Vector3(0,0,0));
}

var centroids = new Array(5400); //real centroids go here
for (var i = 0; i<centroids.length; i++) {
    centroids[i] = Math.abs(Math.sin(i/500))*0xffffff;
} //real consecutive centroids will be relatively close to each other
  //so sin is probably a decent model of it

var fake_centroids = new Array(centroids.length * 2);
for (var i = 1; i<fake_centroids.length; i++) { // convert to 60fps
    fake_centroids[i] = centroids[i-i%2];
}
console.log(fake_centroids);

render();
