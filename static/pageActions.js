
 //Timesout the logo and create the first introduction arrow.
setTimeout(function(){$("#logo").fadeOut()
	    $("#visualizer_intro").fadeIn("slow");},2000);
//Hides the tune arrow before it is shown.
$("#visualizer_intro").hide();

//Hides and shows the left and top bars

function hideLeft(){
    $(".left-rectangle").hide("slide");
    $("#pullright").fadeIn();}

function hideTop(){
    $(".top-rectangle").slideUp("slow");

    $("#pulldown").fadeIn();
    }

function showTop(){
    $(".top-rectangle").slideDown("slow");
    $("#pulldown").fadeOut();}

function showLeft(){
    $(".left-rectangle").slideDown("slow");
    $("#pullright").fadeOut();}



//Hides all the bars by default as you first load the page.
$(".left-rectangle").hide();
$(".top-rectangle").hide();
$("#tune_intro").hide();
$("#textbox").hide();
//Hides the top and left bars once your mouse leaves their area.
$(".top-rectangle").mouseenter(function(){
    }).mouseleave(function(){
	    hideTop()});



//Sets variables to be associated with files
var audio = new Audio();

function play(){
    audio.play();  }

function pause(){
    audio.pause();
}

//handles playing the music
$("#reg1").click(function(){
	pause();
	audio =  new Audio("../static/reg1.mp3");
	audio.load();
	play();
    doAnimate();
    });

$("#reg2").click(function(){
	pause();
        audio = new Audio("../static/reg2.mp3");
	audio.load();
	play();
    doAnimate();
    });

$("#wormhole").click(function(){
	pause();
        audio =  new Audio("../static/superposition.mp3");
	audio.load();
	play();
    doAnimate();
    });

$("#river").click(function(){
	pause();
        audio = new Audio("../static/river.mp3");
	audio.load();
	play();
    doAnimate();
    });

$("#starstuff").click(function(){
	pause();
        audio = new Audio("../static/starstuff.mp3");
	audio.load();
	play();
    doAnimate();
    });

$("#cyprus").click(function(){
	pause();
        audio  = new Audio("../static/cyprus.mp3");
	audio.load();
	play();
    doAnimate();
    });

$("#sands").click(function(){
	pause();
        audio  = new Audio("../static/sands.mp3");
	audio.load();
	play();
    doAnimate();
    });

$("#dubstep").click(function(){
	pause();
        audio  = new Audio("../static/dubstep.mp3");
	audio.load();
	play();
    doAnimate();
    });

$(".left-rectangle").mouseenter(function(){
    }).mouseleave(function(){
	    hideLeft();});


//Loads the navigation bars if the pull bars are clicked.
var introNotDone = true;

$("#pulldown").click(function() {
	showTop();
	$("#visualizer_intro").fadeOut();
	if(introNotDone){
	    $("#tune_intro").fadeIn("slow");
	    introNotDone = false;}});

$("#pullright").click(function() {
	showLeft();
	$("#visualizer_intro").fadeOut();});

$("#about").click(function(){
	$("#about").hide("slide");
	$("#textbox").fadeIn();
    });

$("#textbox").click(function(){
        $("#textbox").hide("slide");
	$("#about").fadeIn("slow");

    });

