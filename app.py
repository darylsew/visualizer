from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import svt

global centroids, frequencies, volumes,reg1centroids, reg1frequencies, reg1volumes, reg2centroids, reg2frequencies, reg2volumes, supercentroids, superfrequencies, supervolumes,rivercentroids, riverfrequencies,rivervolumes,starcentroids, starfrequencies, starvolumes,cypruscentroids, cyprusfrequencies,cyprusvolumes, sandscentroids, sandsfrequencies, sandsvolumes, dubcentroids, dubfrequencies,dubvolumes
app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    #centroids, frequencies, volumes = preProcess()
    if request.method == "POST":
        #If someone pressed the top visualizer
        if str(request.form['vis']) == "1":
            #Redirect to Visualizer 1
            return redirect("/v1")
        elif str(request.form['vis']) == "2":
            return redirect("/v2")
        elif str(request.form['vis']) == "3":
            return redirect("/v3")
        elif str(request.form['vis']) == "4":
            return redirect("/v4")
    return render_template("index.html")

#It seems there's something wrong with having multiple return render_templates in a function.

@app.route("/v1", methods=['GET', 'POST'])
def vis1():
    centroids = []
    frequencies = []
    volumes = []
    song = 0
    if request.method == "POST":
        #If someone pressed the top visualizer
        try:
            if str(request.form['vis']) == "1":
                #Redirect to Visualizer 1
                return redirect("/v1")
            elif str(request.form['vis']) == "2":
                return redirect("/v2")
            elif str(request.form['vis']) == "3":
                return redirect("/v3")
            elif str(request.form['vis']) == "4":
                return redirect("/v4")
        except:
            pass
        try:
        #return data for the right song
            if str(request.form['song']) == "1":
                centroids, frequencies, volumes = reg1centroids, reg1frequencies, reg1volumes
            elif str(request.form['song']) == "2":
                centroids, frequencies, volumes = reg1centroids, reg2frequencies, reg2volumes
            elif str(request.form['song']) == "3":
                centroids, frequencies, volumes = supercentroids, superfrequencies, supervolumes
            elif str(request.form['song']) == "4":
                centroids, frequencies, volumes = rivercentroids, riverfrequencies, rivervolumes 
            elif str(request.form['song']) == "5":
                centroids, frequencies, volumes = starcentroids, starfrequencies, starvolumes
            elif str(request.form['song']) == "6":
                centroids, frequencies, volumes = cypruscentroids, cyprusfrequencies, cyprusvolumes
            elif str(request.form['song']) == "7":
                centroids, frequencies, volumes = sandscentroids, sandsfrequencies, sandsvolumes
            elif str(request.form['song']) == "8":
                centroids, frequencies, volumes = dubcentroids, dubfrequencies, dubvolumes
            song = int(request.form['song'])
        except:
            pass
        #temporary fix
        centroids, frequencies, volumes = starcentroids, starfrequencies, starvolumes
    return render_template("vis1.html", centroids=centroids, frequencies=frequencies, volumes=volumes, song=song)

@app.route("/v2", methods=['GET', 'POST'])
def vis2():
    centroids = []
    frequencies = []
    volumes = []
    song = 0
    if request.method == "POST":
        #If someone pressed the top visualizer
        try:
            if str(request.form['vis']) == "1":
                #Redirect to Visualizer 1
                return redirect("/v1")
            elif str(request.form['vis']) == "2":
                return redirect("/v2")
            elif str(request.form['vis']) == "3":
                return redirect("/v3")
            elif str(request.form['vis']) == "4":
                return redirect("/v4")
        except:
            pass
        try:
        #return data for the right song
            if str(request.form['song']) == "1":
                centroids, frequencies, volumes = reg1centroids, reg1frequencies, reg1volumes
            elif str(request.form['song']) == "2":
                centroids, frequencies, volumes = reg1centroids, reg2frequencies, reg2volumes
            elif str(request.form['song']) == "3":
                centroids, frequencies, volumes = supercentroids, superfrequencies, supervolumes
            elif str(request.form['song']) == "4":
                centroids, frequencies, volumes = rivercentroids, riverfrequencies, rivervolumes 
            elif str(request.form['song']) == "5":
                centroids, frequencies, volumes = starcentroids, starfrequencies, starvolumes
            elif str(request.form['song']) == "6":
                centroids, frequencies, volumes = cypruscentroids, cyprusfrequencies, cyprusvolumes
            elif str(request.form['song']) == "7":
                centroids, frequencies, volumes = sandscentroids, sandsfrequencies, sandsvolumes
            elif str(request.form['song']) == "8":
                centroids, frequencies, volumes = dubcentroids, dubfrequencies, dubvolumes
            song = int(request.form['song'])
        except:
            pass
    return render_template("vis2.html", centroids=centroids, frequencies=frequencies, volumes=volumes, song=song)

@app.route("/v3", methods=['GET', 'POST'])
def vis3():
    centroids = []
    frequencies = []
    volumes = []
    song = 0
    if request.method == "POST":
        #If someone pressed the top visualizer
        try:
            if str(request.form['vis']) == "1":
                #Redirect to Visualizer 1
                return redirect("/v1")
            elif str(request.form['vis']) == "2":
                return redirect("/v2")
            elif str(request.form['vis']) == "3":
                return redirect("/v3")
            elif str(request.form['vis']) == "4":
                return redirect("/v4")
        except:
            pass
        try:
        #return data for the right song
            if str(request.form['song']) == "1":
                centroids, frequencies, volumes = reg1centroids, reg1frequencies, reg1volumes
            elif str(request.form['song']) == "2":
                centroids, frequencies, volumes = reg1centroids, reg2frequencies, reg2volumes
            elif str(request.form['song']) == "3":
                centroids, frequencies, volumes = supercentroids, superfrequencies, supervolumes
            elif str(request.form['song']) == "4":
                centroids, frequencies, volumes = rivercentroids, riverfrequencies, rivervolumes 
            elif str(request.form['song']) == "5":
                centroids, frequencies, volumes = starcentroids, starfrequencies, starvolumes
            elif str(request.form['song']) == "6":
                centroids, frequencies, volumes = cypruscentroids, cyprusfrequencies, cyprusvolumes
            elif str(request.form['song']) == "7":
                centroids, frequencies, volumes = sandscentroids, sandsfrequencies, sandsvolumes
            elif str(request.form['song']) == "8":
                centroids, frequencies, volumes = dubcentroids, dubfrequencies, dubvolumes
            song = int(request.form['song'])
        except:
            pass
    return render_template("vis3.html", centroids=centroids, frequencies=frequencies, volumes=volumes, song=song)

@app.route("/v4", methods=['GET', 'POST'])
def vis4():
    centroids = []
    frequencies = []
    volumes = []
    song = 0
    if request.method == "POST":
        #If someone pressed the top visualizer
        try:
            if str(request.form['vis']) == "1":
                #Redirect to Visualizer 1
                return redirect("/v1")
            elif str(request.form['vis']) == "2":
                return redirect("/v2")
            elif str(request.form['vis']) == "3":
                return redirect("/v3")
            elif str(request.form['vis']) == "4":
                return redirect("/v4")
        except:
            pass
        try:
        #return data for the right song
            if str(request.form['song']) == "1":
                centroids, frequencies, volumes = reg1centroids, reg1frequencies, reg1volumes
            elif str(request.form['song']) == "2":
                centroids, frequencies, volumes = reg1centroids, reg2frequencies, reg2volumes
            elif str(request.form['song']) == "3":
                centroids, frequencies, volumes = supercentroids, superfrequencies, supervolumes
            elif str(request.form['song']) == "4":
                centroids, frequencies, volumes = rivercentroids, riverfrequencies, rivervolumes 
            elif str(request.form['song']) == "5":
                centroids, frequencies, volumes = starcentroids, starfrequencies, starvolumes
            elif str(request.form['song']) == "6":
                centroids, frequencies, volumes = cypruscentroids, cyprusfrequencies, cyprusvolumes
            elif str(request.form['song']) == "7":
                centroids, frequencies, volumes = sandscentroids, sandsfrequencies, sandsvolumes
            elif str(request.form['song']) == "8":
                centroids, frequencies, volumes = dubcentroids, dubfrequencies, dubvolumes
            song = int(request.form['song'])
        except:
            pass
    return render_template("vis4.html", centroids=centroids, frequencies=frequencies, volumes=volumes, song=song)
#if we use fileIO preprocessing
def preProcess():
    pass

if __name__=="__main__":
    centroids, frequencies, volumes = svt.processWav("wubwub.wav", 1)
    reg1centroids, reg1frequencies, reg1volumes = svt.processWav("./static/reg1.wav", 1)
    reg2centroids, reg2frequencies, reg2volumes = svt.processWav("./static/reg2.wav", 1)
    cypruscentroids, cyprusfrequencies,cyprusvolumes = svt.processWav("./static/cyprus.wav", 1)
    dubcentroids, dubfrequencies,dubvolumes = svt.processWav("./static/dubstep.wav", 1)
    rivercentroids, riverfrequencies,rivervolumes = svt.processWav("./static/river.wav", 1)
    sandscentroids, sandsfrequencies, sandsvolumes = svt.processWav("./static/sands.wav", 1)
    starcentroids, starfrequencies, starvolumes = svt.processWav("./static/starstuff.wav", 1)
    supercentroids, superfrequencies, supervolumes = svt.processWav("./static/superposition.wav", 1) #wormhole
    app.run(debug=True)
