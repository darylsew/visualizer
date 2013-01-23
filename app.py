from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import svt

global centroids, frequencies, volumes,reg1centroids, reg1frequencies, reg1volumes, reg2centroids, reg2frequencies, reg2volumes, supercentroids, superfrequencies, supervolumes,rivercentroids, riverfrequencies,rivervolumes,starcentroids, starfrequencies, starvolumes,cypruscentroids, cyprusfrequencies,cyprusvolumes, sandscentroids, sandsfrequencies, sandsvolumes, dubcentroids, dubfrequencies,dubvolumes

#centroids, frequencies, volumes = svt.processWav("wubwub.wav", 1)
reg1centroids, reg1frequencies, reg1volumes = svt.processWav("./static/reg1.wav", 1)
reg2centroids, reg2frequencies, reg2volumes = svt.processWav("./static/reg2.wav", 1)
cypruscentroids, cyprusfrequencies,cyprusvolumes = svt.processWav("./static/cyprus.wav", 1)
dubcentroids, dubfrequencies,dubvolumes = svt.processWav("./static/dubstep.wav", 1)
rivercentroids, riverfrequencies,rivervolumes = svt.processWav("./static/river.wav", 1)
sandscentroids, sandsfrequencies, sandsvolumes = svt.processWav("./static/sands.wav", 1)
starcentroids, starfrequencies, starvolumes = svt.processWav("./static/starstuff.wav", 1)
supercentroids, superfrequencies, supervolumes = svt.processWav("./static/superposition.wav", 1) #wormhole

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



@app.route("/v1", methods=['GET', 'POST'])
def vis1():
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
        #return data for the right song
        elif str(request.form['song'] == "1"):
            print "Song 1 Picked!"
            return render_template("vis1.html", 
                    centroids=reg1centroids, 
                    frequencies=reg1frequencies, 
                    volumes=reg1volumes,
                    song="1")
        elif str(request.form['song'] == "2"):
            return render_template("vis1.html",
                    centroids=reg2centroids,
                    frequencies=reg2frequencies,
                    volumes=reg2volumes,
                    song="2")
        elif str(request.form['song'] == "3"):
            return render_template("vis1.html",
                    centroids=supercentroids,
                    frequencies=superfrequencies,
                    volumes=supervolumes,
                    song="3")
        elif str(request.form['song'] == "4"):
            return render_template("vis1.html",
                    centroids=rivercentroids,
                    frequencies=riverfrequencies,
                    volumes=rivervolumes,
                    song="4")
        elif str(request.form['song'] == "5"):
            return render_template("vis1.html",
                    centroids=starcentroids,
                    frequencies=starfrequencies,
                    volumes=starvolumes,
                    song="5")
        elif str(request.form['song'] == "6"):
            return render_template("vis1.html",
                    centroids=cypruscentroids,
                    frequencies=cyprusfrequencies,
                    volumes=cyprusvolumes,
                    song="6")
        elif str(request.form['song'] == "7"):
            return render_template("vis1.html",
                    centroids=sandscentroids,
                    frequencies=sandsfrequencies,
                    volumes=sandsvolumes,
                    song="7")
        elif str(request.form['song'] == "8"):
            return render_template("vis1.html",
                    centroids=dubcentroids,
                    frequencies=dubfrequencies,
                    volumes=dubvolumes,
                    song="8")
    return render_template("vis1.html", song="0")

@app.route("/v2", methods=['GET', 'POST'])
def vis2():
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
        #return data for the right song
        elif str(request.form['song'] == "1"):
            return render_template("vis2.html", 
                    centroids=reg1centroids, 
                    frequencies=reg1frequencies, 
                    volumes=reg1volumes,
                    song="1")
        elif str(request.form['song'] == "2"):
            return render_template("vis2.html",
                    centroids=reg2centroids,
                    frequencies=reg2frequencies,
                    volumes=reg2volumes,
                    song="2")
        elif str(request.form['song'] == "3"):
            return render_template("vis2.html",
                    centroids=supercentroids,
                    frequencies=superfrequencies,
                    volumes=supervolumes,
                    song="3")
        elif str(request.form['song'] == "4"):
            return render_template("vis2.html",
                    centroids=rivercentroids,
                    frequencies=riverfrequencies,
                    volumes=rivervolumes,
                    song="4")
        elif str(request.form['song'] == "5"):
            return render_template("vis2.html",
                    centroids=starcentroids,
                    frequencies=starfrequencies,
                    volumes=starvolumes,
                    song="5")
        elif str(request.form['song'] == "6"):
            return render_template("vis2.html",
                    centroids=cypruscentroids,
                    frequencies=cyprusfrequencies,
                    volumes=cyprusvolumes,
                    song="6")
        elif str(request.form['song'] == "7"):
            return render_template("vis2.html",
                    centroids=sandscentroids,
                    frequencies=sandsfrequencies,
                    volumes=sandsvolumes,
                    song="7")
        elif str(request.form['song'] == "8"):
            return render_template("vis2.html",
                    centroids=dubcentroids,
                    frequencies=dubfrequencies,
                    volumes=dubvolumes,
                    song="8")
    return render_template("vis2.html", song="0")

@app.route("/v3", methods=['GET', 'POST'])
def vis3():
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
        #return data for the right song
        elif str(request.form['song'] == "1"):
            return render_template("vis3.html", 
                    centroids=reg1centroids, 
                    frequencies=reg1frequencies, 
                    volumes=reg1volumes,
                    song="1")
        elif str(request.form['song'] == "2"):
            return render_template("vis3.html",
                    centroids=reg2centroids,
                    frequencies=reg2frequencies,
                    volumes=reg2volumes,
                    song="2")
        elif str(request.form['song'] == "3"):
            return render_template("vis3.html",
                    centroids=supercentroids,
                    frequencies=superfrequencies,
                    volumes=supervolumes,
                    song="3")
        elif str(request.form['song'] == "4"):
            return render_template("vis3.html",
                    centroids=rivercentroids,
                    frequencies=riverfrequencies,
                    volumes=rivervolumes,
                    song="4")
        elif str(request.form['song'] == "5"):
            return render_template("vis3.html",
                    centroids=starcentroids,
                    frequencies=starfrequencies,
                    volumes=starvolumes,
                    song="5")
        elif str(request.form['song'] == "6"):
            return render_template("vis3.html",
                    centroids=cypruscentroids,
                    frequencies=cyprusfrequencies,
                    volumes=cyprusvolumes,
                    song="6")
        elif str(request.form['song'] == "7"):
            return render_template("vis3.html",
                    centroids=sandscentroids,
                    frequencies=sandsfrequencies,
                    volumes=sandsvolumes,
                    song="7")
        elif str(request.form['song'] == "8"):
            return render_template("vis3.html",
                    centroids=dubcentroids,
                    frequencies=dubfrequencies,
                    volumes=dubvolumes,
                    song="8")
    return render_template("vis3.html", song="0")

@app.route("/v4", methods=['GET', 'POST'])
def vis4():
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
        #return data for the right song
        elif str(request.form['song'] == "1"):
            return render_template("vis4.html", 
                    centroids=reg1centroids, 
                    frequencies=reg1frequencies, 
                    volumes=reg1volumes,
                    song="1")
        elif str(request.form['song'] == "2"):
            return render_template("vis4.html",
                    centroids=reg2centroids,
                    frequencies=reg2frequencies,
                    volumes=reg2volumes,
                    song="2")
        elif str(request.form['song'] == "3"):
            return render_template("vis4.html",
                    centroids=supercentroids,
                    frequencies=superfrequencies,
                    volumes=supervolumes,
                    song="3")
        elif str(request.form['song'] == "4"):
            return render_template("vis4.html",
                    centroids=rivercentroids,
                    frequencies=riverfrequencies,
                    volumes=rivervolumes,
                    song="4")
        elif str(request.form['song'] == "5"):
            return render_template("vis4.html",
                    centroids=starcentroids,
                    frequencies=starfrequencies,
                    volumes=starvolumes,
                    song="5")
        elif str(request.form['song'] == "6"):
            return render_template("vis4.html",
                    centroids=cypruscentroids,
                    frequencies=cyprusfrequencies,
                    volumes=cyprusvolumes,
                    song="6")
        elif str(request.form['song'] == "7"):
            return render_template("vis4.html",
                    centroids=sandscentroids,
                    frequencies=sandsfrequencies,
                    volumes=sandsvolumes,
                    song="7")
        elif str(request.form['song'] == "8"):
            return render_template("vis4.html",
                    centroids=dubcentroids,
                    frequencies=dubfrequencies,
                    volumes=dubvolumes,
                    song="8")
    return render_template("vis4.html", song="0")

#if we use fileIO preprocessing
def preProcess():
    pass

if __name__=="__main__":
    app.debug=True
    app.run()
