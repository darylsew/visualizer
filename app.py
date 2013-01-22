from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import svt

app=Flask(__name__)

@app.route("/")
def index():
    centroids, frequencies, volumes = svt.processWav("wubwub.wav", 1)
    #centroids, frequencies, volumes = preProcess()
    return render_template("testing.html",
                            centroids=centroids,
                            frequencies=frequencies,
                            volumes=volumes)
def preProcess():
    pass

if __name__=="__main__":
    app.debug=True
    app.run()
