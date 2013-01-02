import wave

f = wave.open("wubwub.wav", 'r')

print f.getparams()

print f.readframes(20)
