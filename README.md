Visualizer
==========
Group members:
pd6: Eric Cerny, Hon Wei Khor
pd7: Daryl Sew, Peter Jasko

What we're going to do:
Take a music file and visualize it, let the user play around with some settings for the visualization. We'll decide on additional features later on in the project.

How we're going to do it:
Using chaco and scipy/numpy (contained within the Enthought library for scientific computing) for fourier transform analysis of wav files.

Resources/dependencies (we have a LOT of dependencies):

Songs will be from the user's own music library; several royalty-free songs will be provided for demonstration purposes.
Tkinter (sudo apt-get install python-tk)
WCKGraph
Tkinter and WCKGraph are temporary dependencies.

wavepy (sudo pip install wave)
enable (sudo apt-get install python-enable)
pyaudio (sudo apt-get install python-pyaudio)
python enthought (python ets/ets.py)
scipy/numpy (sudo apt-get install python-numpy python-scipy)
chaco (sudo pip install chaco)

We're not really going to use the branch workflow until we agree on a workflow model (presumably in the next few days).

As for the proof of concept code, we have code that we know will generate the data needed for visualization from a wav file, but it's a huge pain to get all the dependencies together and working, so it's not exactly proof of concept code. Specifically, I'm having trouble setting up the python enthought library for scientific computing (once that's set up, we're good). Proof that this will work can be found here: http://code.enthought.com/projects/chaco/pu-audio-spectrum.html. In case enthought doesn't work out, plan B is Method 3 in waveproof.py; taken from http://www.swharden.com/blog/2010-03-05-realtime-fft-graph-of-audio-wav-file-or-microphone-input-with-python-scipy-and-wckgraph/, this is proof that Method 3 will work: http://www.swharden.com/blog/images/python-real-time-tk-wav-fft.gif (also, in the comments section of that page someone confirmed it worked for them).
 
