

	var camera, scene, renderer;
	var centerSphere,orb1,orb2,orb3,sphdist,camdist;
    var mesh,geometry, material;
	var startTime;
	var centroids, volumes, frequencies, counter, maxlen;
	var alpha, beta1, beta2, gamma1, gamma2;
	var light, ambientLight;
    init();
    animate();

    function init() {
		alpha = 0;//sphere-sphere rot alignment
		beta1 = 45;//camera rot alignment
		beta2 = 75;//camera rot alignment
		gamma1 = 35;//lighting rot alignment
		gamma2 = 123;//lighting rot alignment
		sphdist = 500;//distance between orbital spheres and centersphere
		litdist = 350;//D_(lit to <0,0,0>)
		camdist = 1200;//D_(cam to <0,0,0>)
		startTime = Date.now();
		centroids = {{centroids}};
		volumes = {{volumes}};
		frequencies = {{frequencies}};
		counter = 0;
		maxlen = centroids.length;
		material = new THREE.MeshLambertMaterial( {color: 0xff8800} );
		/*camera*/
		camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 1, 10000 );
/*		camera.position.x = camdist*Math.cos(beta1*Math.PI/180);
		camera.position.y = camdist*Math.sin(beta1*Math.PI/180)*Math.cos(beta2*Math.PI/180);
		camera.position.z = camdist*Math.sin(beta1*Math.PI/180)*Math.sin(beta2*Math.PI/180);*/
		camera.position.x = camdist*Math.cos(beta1*Math.PI/180);
		camera.position.y = camdist*Math.sin(beta1*Math.PI/180)/2;
		camera.position.z = (camera.position.y/Math.abs(camera.position.y))*Math.sqrt(Math.pow(camdist,2)-Math.pow(camera.position.x,2)+Math.pow(camera.position.y,2));
		camera.lookAt(new THREE.Vector3(0,0,0));
		/*spheres*/
		centerSphere=new THREE.Mesh(new THREE.SphereGeometry(300,14,7), material);
		centerSphere.position.x = 0;
		centerSphere.position.y = 0;
		centerSphere.position.z = 0;
		orb1=new THREE.Mesh(new THREE.SphereGeometry(75,14,7), material);
		orb1.position.x = sphdist*Math.cos(alpha+Math.PI/3*0);
		orb1.position.y = sphdist*Math.sin(alpha+Math.PI/3*0);
		orb2=new THREE.Mesh(new THREE.SphereGeometry(75,14,7), material);
		orb2.position.x = sphdist*Math.cos(alpha+Math.PI/3*2);
		orb2.position.y = sphdist*Math.sin(alpha+Math.PI/3*2);
		orb3=new THREE.Mesh(new THREE.SphereGeometry(75,14,7), material);
		orb3.position.x = sphdist*Math.cos(alpha+Math.PI/3*4);
		orb3.position.y = sphdist*Math.sin(alpha+Math.PI/3*4);
		/*lights*/
		light = new THREE.PointLight(0xffffff);
		light.position.y = litdist*Math.cos(gamma1*Math.PI/180);
		light.position.x = litdist*Math.sin(gamma1*Math.PI/180);
		light.intensity=2;
		ambientLight = new THREE.AmbientLight(0x999999);
		/*scene and additions*/
		scene = new THREE.Scene();
		scene.add(centerSphere);
		scene.add(orb1);
		scene.add(orb2);
		scene.add(orb3);
		scene.add(light);
		scene.add(ambientLight);
		renderer = new THREE.CanvasRenderer();
        renderer.setSize( window.innerWidth, window.innerHeight );
        document.body.appendChild( renderer.domElement );
    }
	function orbsfreqjitter(){
		var arrgh = frequencies[counter];
		jumpy0 = 0.0;
		jumpy1 = 0.0;
		jumpy2 = 0.0;
		for (var i = 0; i < arrgh.length; i++){
			if((i%3) == 0){jumpy0 += arrgh[i];}
			if(i%3 == 1){jumpy1 += arrgh[i];}
			if(i%3 == 2){jumpy2 += arrgh[i];}
		}
		jumpy0 /= (arrgh.length/3);
		jumpy1 /= (arrgh.length/3);
		jumpy2 /= (arrgh.length/3);
		return [jumpy0-.5,jumpy1-.5, jumpy2-.5];
	}
	function orbsreposition(){
		var whee = orbsfreqjitter();
		orb1.position.x = sphdist*Math.cos((alpha+0)*Math.PI/180);
		orb1.position.y = sphdist*Math.sin((alpha+0)*Math.PI/180);
		orb1.position.z = whee[0];
		orb1.rotation.z +=6*Math.PI/180;
		orb2.position.x = sphdist*Math.cos((alpha+120)*Math.PI/180);
		orb2.position.y = sphdist*Math.sin((alpha+120)*Math.PI/180);
		orb2.position.z = whee[1];
		orb2.rotation.z +=6*Math.PI/180;
		orb3.position.x = sphdist*Math.cos((alpha+240)*Math.PI/180);
		orb3.position.y = sphdist*Math.sin((alpha+240)*Math.PI/180);
		orb3.position.z = whee[2];
		orb3.rotation.z +=6*Math.PI/180;
		centerSphere.rotation.z +=3*Math.PI/180;
		centerSphere.scale.x = volumes[counter];
		centerSphere.scale.y = volumes[counter];
		centerSphere.scale.z = volumes[counter];
		hexString = (Math.floor(centroids[counter]*16777215)).toString(16);
		centerSphere.material.color.setHex(parseInt(hexString, 16));
		orb1.material.color.setHex(parseInt(hexString, 16));
		orb2.material.color.setHex(parseInt(hexString, 16));
		orb3.material.color.setHex(parseInt(hexString, 16));
	}
	function camreposition(){
/*		camera.position.x = camdist*Math.cos(beta1*Math.PI/180);
		camera.position.y = camdist*Math.sin(beta1*Math.PI/180)*Math.sin(beta2*Math.PI/180);
		camera.position.z = camdist*Math.sin(beta1*Math.PI/180)*Math.cos(beta2*Math.PI/180);*/
		camera.position.x = camdist*Math.cos(beta1*Math.PI/180);
		camera.position.y = camdist*Math.sin(beta1*Math.PI/180)/2;
		camera.position.z = (camera.position.y/Math.abs(camera.position.y))*Math.sqrt(Math.pow(camdist,2)-Math.pow(camera.position.x,2)+Math.pow(camera.position.y,2));
		camera.lookAt(new THREE.Vector3(0,0,0));
	}
	function lightrepos(){
		light.position.y = litdist*Math.cos(gamma1*Math.PI/180);
		light.position.x = litdist*Math.sin(gamma1*Math.PI/180);
	}
    function animate() {

        // note: three.js includes requestAnimationFrame shim
        requestAnimationFrame( animate );
		counter = (counter+1)%maxlen;
		alpha = (alpha + 15)%360;
		beta1 = (beta1 + 1.5)%360;
//		beta2 = (beta2 + 1.5)%360;
		gamma1 = (gamma1 + 357.5) %360;
		orbsreposition();
		camreposition();
		lightrepos();
        renderer.render( scene, camera );
    }
