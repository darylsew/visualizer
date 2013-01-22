from flask import request, Flask, render_template, url_for, redirect, request
import urllib2,json
#import svt
from random import random

app = Flask(__name__)

centroids = []
for i in range(2000):
    centroids.append(random())
volumes = []
for i in range(2000):
    volumes.append(random())
frequencies = []
for i in range(2000):
    frequencies.append([])
for i in frequencies:
    for j in range(500):
        i.append(random())

@app.route("/")
def index():
    return render_template("spectrum.html",
                           centroids=centroids,
                           frequencies=frequencies,
                           volumes=volumes)

if __name__ == "__main__":
    app.debug=True
    app.run()
