
 //Timesout the logo and create the first introduction arrow.
setTimeout(function(){$("#logo").fadeOut()
	    $("#tune_intro").fadeIn("slow");},2000);
//Hides the tune arrow before it is shown.
$("#tune_intro").hide();

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
$("#visualizer_intro").hide();

//Hides the top and left bars once your mouse leaves their area.
$(".top-rectangle").mouseenter(function(){
    }).mouseleave(function(){
	    hideTop()});



//Sets variables to be associated with files
var audio = new Audio();
var reg1Audio = new Audio("../static/reg1.wav");
var reg2Audio = new Audio("../static/reg2.wav");
var starstuffAudio = new Audio("../static/starstuff.wav");
var superpositionAudio = new Audio("../static/superposition.wav");
var cyprusAudio = new Audio("../static/cyprus.wav");
var sandsAudio = new Audio("../static/sands.wav");
var dubstepAudio = new Audio("../static/dubstep.wav");
var riverAudio = new Audio("../static/river.wav");


function play(){
    audio.play();  }

function pause(){
    audio.pause();
}

//handles playing the music
$("#reg1").click(function(){
	pause();
	audio = reg1Audio;
	audio.load();
	play();
    });

$("#reg2").click(function(){
	pause();
        audio = reg2Audio;
	audio.load();
	play();
    });

$("#wormhole").click(function(){
	pause();
        audio = superpositionAudio;
	audio.load();
	play();
    });

$("#river").click(function(){
	pause();
        audio = riverAudio;
	audio.load();
	play();
    });

$("#starstuff").click(function(){
	pause();
        audio = starstuffAudio;
	audio.load();
	play();
    });

$("#cyprus").click(function(){
	pause();
        audio = cyprusAudio;
	audio.load();
	play();
    });

$("#sands").click(function(){
	pause();
        audio = sandsAudio;
	audio.load();
	play();
    });

$("#dubstep").click(function(){
	pause();
        audio = dubstepAudio;
	audio.load();
	play();
    });

$(".left-rectangle").mouseenter(function(){
    }).mouseleave(function(){
	    hideLeft();});


//Loads the navigation bars if the pull bars are clicked.
var introNotDone = true;

$("#pulldown").click(function() {
	showTop();
	$("#tune_intro").fadeOut();
	if(introNotDone){
	    $("#visualizer_intro").fadeIn("slow");
	    introNotDone = false;}});

$("#pullright").click(function() {
	showLeft();
	$("#visualizer_intro").fadeOut();});
