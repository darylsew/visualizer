Visualizer
==========
*Group members:*
<li>pd6: Eric Cerny, Hon Wei Khor</li>
<li>pd7: Daryl Sew, Peter Jasko</li>

*What we're going to do:*
Take a music file and visualize it, let the user play around with some settings for the visualization. We'll decide on additional features later on in the project.

*How we're going to do it:*
Using chaco and scipy/numpy (contained within the Enthought library for scientific computing) for fourier transform analysis of wav files.

*Resources/dependencies (we have a LOT of dependencies):*

Songs will be from the user's own music library; several royalty-free songs will be provided for demonstration purposes.
1. Tkinter (sudo apt-get install python-tk)
2. WCKGraph (Tkinter and WCKGraph are temporary dependencies.)
3. wavepy (sudo pip install wave)
4. python enthought (python ets/ets.py) Enthought includes enable, scipy/numpy, and chaco; however, I haven't been able to get it working. It's a pretty awesome, well supported library for scientific computing, so I have faith in it, but I do have a plan B.
5. enable (sudo apt-get install python-enable)
6. scipy/numpy (sudo apt-get install python-numpy python-scipy)
7. chaco (sudo pip install chaco)
8. pyaudio (sudo apt-get install python-pyaudio)

We're not really going to use the branch workflow until we agree on a workflow model (presumably in the next few days). We'll have a formal writeup of our workflow and of the semantics of design we'll stick to sometime soon.

As for the proof of concept code, we have code that we know will generate the data needed for visualization from a wav file, but it's a huge pain to get all the dependencies together and working, so it's not exactly proof of concept code. Specifically, I'm having trouble setting up the python enthought library for scientific computing (once that's set up, we're good). Proof that this will work can be found [here](http://code.enthought.com/projects/chaco/pu-audio-spectrum.html). In case enthought doesn't work out, plan B is Method 3 in waveproof.py; taken from [here](http://www.swharden.com/blog/2010-03-05-realtime-fft-graph-of-audio-wav-file-or-microphone-input-with-python-scipy-and-wckgraph/), [this](http://www.swharden.com/blog/images/python-real-time-tk-wav-fft.gif) is proof that Method 3 will work. (also, in the comments section of that page someone confirmed it worked for them). 
