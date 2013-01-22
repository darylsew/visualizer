var scene = new THREE.Scene();

var WIDTH = 800;
var HEIGHT = 600;
var camera = new THREE.PerspectiveCamera(75, WIDTH/HEIGHT, 0.1, 1000);
camera.position.z = 9;
camera.position.x = -5;

var renderer = new THREE.WebGLRenderer();
renderer.setSize(WIDTH, HEIGHT);
document.body.appendChild(renderer.domElement);

var planeGeometry = new THREE.PlaneGeometry(150,150,0,0);
var planeMaterial = new THREE.MeshPhongMaterial({ color:0xf0f0f0 });
var plane = new THREE.Mesh(planeGeometry, planeMaterial);
scene.add(plane);
plane.position.z = -21;

var spotlight = new THREE.SpotLight(0xFFFFFF);
spotlight.position.z = 80;
scene.add(spotlight);

var cubes = new Array(15);
for (var i = 0; i<15 ; i++) {
    cubes[i] = new Array(10);
}

var materials = new Array(150);
for (var i = 0; i<150; i++) {
    materials[i] = new THREE.MeshPhongMaterial({ color:0xf0f0f0 });
}
var cubeGeometry = new THREE.CubeGeometry(0.5,0.5,0.5);

x = -7; mat = 0;
for (var i = 0; i<15; i++) {
    y = -4;
    for (var j = 0; j<10; j++) {
	cubes[i][j] = new THREE.Mesh(cubeGeometry, materials[mat]);
	scene.add(cubes[i][j]);
	cubes[i][j].position.x=x;
	cubes[i][j].position.y=y;
	y++;
	mat++;
    }
    x++;
}


//DUMMY VALUES
var centroids = new Array(5400); //real centroids go here
for (var i = 0; i<centroids.length; i++) {
    centroids[i] = Math.abs(Math.sin(i/100));
} //real consecutive centroids will be relatively close to each other
  //so sin is probably a decent model of it

var fake_centroids = new Array(centroids.length * 2);
for (var i = 1; i<fake_centroids.length; i++) { // convert to 60fps
    fake_centroids[i] = centroids[i-i%2];
}

var frequencies = new Array(2700); //real frequencies go here
for (var i = 0; i<frequencies.length; i++) {
    frequencies[i] = Math.abs(Math.cos(i/100));
}
var fake_frequencies = new Array(frequencies.length * 4);
for (var i = 0; i<fake_frequencies.length; i++) {
    fake_frequencies[i] = frequencies[i-i%4];
    fake_frequencies[i] = Math.floor(fake_frequencies[i] * 14);
}

var vols = new Array(5400);
for (var i = 0; i<vols.length; i++) {
    vols[i] = Math.abs(Math.sin(i/80));
}
var fake_vols = new Array(vols.length * 2);
for (var i = 0; i<fake_vols.length; i++) {
    fake_vols[i] = vols[i-i%2];
    fake_vols[i] = Math.floor(fake_vols[i] * 9);
}

function light_column(freq, vol) {
    for (var i = 0; i<=vol; i++) {
	if (i >= 7) {
	    cubes[freq][i].material.color.setHex(0xff0000);
	}
	else{
	    cubes[freq][i].material.color.setHex(0x0000ff);
	}
    }
    setTimeout(function() {
	    for (var i = 0; i <= 9; i++) {
		cubes[freq][i].material.color.setHex(0xf0f0f0);
	    }
	}, 400);
}

function light_region(freq, vol) {
    light_column(freq, vol);
    if (vol >= 3) {
	if (freq != 0) {
	    light_column(freq-1, vol-2);
	}
	if (freq != 14) {
	    light_column(freq+1, vol-2);
	}
    }
    if (vol >= 5) {
	if (freq != 0) {
	    light_column(freq-1, vol-4);
	}
	if (freq != 14) {
	    light_column(freq+1, vol-4);
	}
    }
}

var index = 0;
function render() {
    requestAnimationFrame(render);
    renderer.render(scene,camera);
    //    camera.position.x = 3*Math.cos(index/200);
    //    camera.position.y = 3*Math.sin(index/200);
    spotlight.position.z = 60 + 30*fake_centroids[index];
    camera.lookAt(new THREE.Vector3(-2,0,0));
    light_region(fake_frequencies[index],fake_vols[index]);
    index++;
}

render();