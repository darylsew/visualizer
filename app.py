from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import svt

global centroids, frequencies, volumes,reg1centroids, reg1frequencies, reg1volumes, reg2centroids, reg2frequencies, reg2volumes, cypruscentroids, cyprusfrequencies,cyprusvolumes, dubcentroids, dubfrequencies,dubvolumes,rivercentroids, riverfrequencies,rivervolumes,sandscentroids, sandsfrequencies, sandsvolumes,starcentroids, starfrequencies, starvolumes,supercentroids, superfrequencies, supervolumes

centroids, frequencies, volumes = svt.processWav("wubwub.wav", 1)
#reg1centroids, reg1frequencies, reg1volumes = svt.processWav("./static/reg1.wav", 1)
#reg2centroids, reg2frequencies, reg2volumes = svt.processWav("./static/reg2.wav", 1)
#cypruscentroids, cyprusfrequencies,cyprusvolumes = svt.processWav("./static/cyprus.wav", 1)
#dubcentroids, dubfrequencies,dubvolumes = svt.processWav("./static/dubstep.wav", 1)
#rivercentroids, riverfrequencies,rivervolumes = svt.processWav("./static/river.wav", 1)
#sandscentroids, sandsfrequencies, sandsvolumes = svt.processWav("./static/sands.wav", 1)
#starcentroids, starfrequencies, starvolumes = svt.processWav("./static/starstuff.wav", 1)
#supercentroids, superfrequencies, supervolumes = svt.processWav("./static/superposition.wav", 1)





app=Flask(__name__)

@app.route("/")
def index():
    #centroids, frequencies, volumes = preProcess()

    return render_template("testing.html",
                            centroids=centroids,
                            frequencies=frequencies,
                            volumes=volumes)
#if we use fileIO preprocessing
def preProcess():
    pass

if __name__=="__main__":
    app.debug=True
    app.run()
