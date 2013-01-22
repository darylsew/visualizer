from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import svt

global centroids, frequencies, volumes
centroids, frequencies, volumes = svt.processWav("wubwub.wav", 1)
#print "before the routine"
app=Flask(__name__)

@app.route("/")
def index():
    #centroids, frequencies, volumes = preProcess()
    #print "after the routine"
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
