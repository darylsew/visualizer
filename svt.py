#!/usr/bin/env python
der the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
# Renamed to svt to keep separate from the wav2png.py script
# 
# Based on wav2png.py by Bram de Jong <bram.dejong at domain.com where domain in gmail>
# From http://freesound.iua.upf.edu/blog/?p=10
#
"""
svt.py [options] filename.wav
The options the script takes are:
<ul>
 <li>-a = output waveform image (default input filename + _w.png)</li>
 <li>-s = output spectrogram image (default input filename + _s.png)</li>
 <li>-w = image width in pixels (default 500)</li>
 <li>-h = image height in pixels (default 170)</li>
 <li>-f = fft size, power of 2 (default 2048)</li>
 <li>-m = maximum frequency to draw, in Hz (default 22050)</li>
 <li>-o = 1 if you want to draw the waveform too
</ul>
"""
 
import optparse, math, sys
import scikits.audiolab as audiolab
import ImageFilter, ImageChops, Image, ImageDraw, ImageColor
import numpy

#For music visualization, this class is more or less irrelevant.
class TestAudioFile(object):
    """A class that mimics audiolab.sndfile but generates noise instead of reading
    a wave file. Additionally it can be told to have a "broken" header and thus crashing
    in the middle of the file. Also useful for testing ultra-short files of 20 samples."""

    def __init__(self, num_frames, has_broken_header=False):
        self.seekpoint = 0
        self.num_frames = num_frames
        self.has_broken_header = has_broken_header
 
    def seek(self, seekpoint):
        self.seekpoint = seekpoint
 
    def get_nframes(self):
        return self.num_frames
 
    def get_samplerate(self):
        return 44100
 
    def get_channels(self):
        return 1
 
    def read_frames(self, frames_to_read):
        if self.has_broken_header and self.seekpoint + frames_to_read > self.num_frames / 2:
            raise IOError()
 
        num_frames_left = self.num_frames - self.seekpoint
        will_read = num_frames_left if num_frames_left < frames_to_read else frames_to_read
        self.seekpoint += will_read
        return numpy.random.random(will_read)*2 - 1 
 
 
class AudioProcessor(object):
    def __init__(self, audio_file, fft_size, channel, window_function=numpy.ones):
        self.fft_size = fft_size
        self.window = window_function(self.fft_size)
        self.audio_file = audio_file
        self.frames = audio_file.get_nframes()
        self.samplerate = audio_file.get_samplerate()
        self.channels = audio_file.get_channels()
        self.spectrum_range = None
        self.lower = 100
        self.higher = 22050
        self.lower_log = math.log10(self.lower)
        self.higher_log = math.log10(self.higher)
        self.clip = lambda val, low, high: min(high, max(low, val))
        self.channel = channel
    
    #returns a number of samples from the audio file. 
    def read(self, start, size, resize_if_less=False):
        """ read size samples starting at start, if resize_if_less is True and less than size
        samples are read, resize the array to size and fill with zeros """
 
        # number of zeros to add to start and end of the buffer
        add_to_start = 0
        add_to_end = 0
 
        if start < 0:
            # the first FFT window starts centered around zero
            if size + start <= 0:
                return numpy.zeros(size) if resize_if_less else numpy.array([])
            else:
                self.audio_file.seek(0)
 
                add_to_start = -start # remember: start is negative!
                to_read = size + start
 
                if to_read > self.frames:
                    add_to_end = to_read - self.frames
                    to_read = self.frames
        else:
            self.audio_file.seek(start)
 
            to_read = size
            if start + to_read >= self.frames:
                to_read = self.frames - start
                add_to_end = size - to_read
 
        try:
            samples = self.audio_file.read_frames(to_read)
        except IOError:
            # this can happen for wave files with broken headers...
            return numpy.zeros(size) if resize_if_less else numpy.zeros(2)
 
        # select which channel to draw
        if self.channels > 1:
            if self.channel==1:
                samples = samples[:,0]
            if self.channel==2:
                samples = samples[:,1]
 
        if resize_if_less and (add_to_start > 0 or add_to_end > 0):
            if add_to_start > 0:
                samples = numpy.concatenate((numpy.zeros(add_to_start), samples), axis=1)
 
            if add_to_end > 0:
                samples = numpy.resize(samples, size)
                samples[size - add_to_end:] = 0
 
        return samples
 
    """
    The spectral centroid is a measure used in digital signal processing to characterise
    a spectrum. It indicates where the "center of mass" of the spectrum is. Perceptually,
    it has a robust connection with the impression of "brightness" of a sound. It is calculated
    as the weighted mean of the frequencies present in the signal, determined using a Fourier
    transform, with their magnitudes as the wiehgts.
    The spectral centroid is widely used in digital audio and music processing as an automatic
    measure of musical timbre. -Wikipedia
    
    Probably extremely useful for visualization.
    """
    def spectral_centroid(self, seek_point, spec_range=120.0):
        """ starting at seek_point read fft_size samples, and calculate the spectral centroid """
        
        samples = self.read(seek_point - self.fft_size/2, self.fft_size, True)
 
        samples *= self.window
        fft = numpy.fft.fft(samples)
        spectrum = numpy.abs(fft[:fft.shape[0] / 2 + 1]) / float(self.fft_size) # normalized abs(FFT) between 0 and 1
        length = numpy.float64(spectrum.shape[0])
 
        # scale the db spectrum from [- spec_range db ... 0 db] > [0..1]
        db_spectrum = ((20*(numpy.log10(spectrum + 1e-30))).clip(-spec_range, 0.0) + spec_range)/spec_range
 
        energy = spectrum.sum()
        spectral_centroid = 0
 
        if energy > 1e-20:
            # calculate the spectral centroid
 
            if self.spectrum_range == None:
                self.spectrum_range = numpy.arange(length)
 
            spectral_centroid = (spectrum * self.spectrum_range).sum() / (energy * (length - 1)) * self.samplerate * 0.5
 
            # clip > log10 > scale between 0 and 1
            spectral_centroid = (math.log10(self.clip(spectral_centroid, self.lower, self.higher)) - self.lower_log) / (self.higher_log - self.lower_log)
 
        return (spectral_centroid, db_spectrum)
 
    #Goes through the samples and finds the min and max amplitudes; used to draw the waveform.
    #This function is probably what I need to use to output amplitudes to a visualizer..
    def peaks(self, start_seek, end_seek):
        """ read all samples between start_seek and end_seek, then find the minimum and maximum peak
        in that range. Returns that pair in the order they were found. So if min was found first,
        it returns (min, max) else the other way around. """
 
        # larger blocksizes are faster but take more mem...
        # Aha, Watson, a clue, a tradeof!
        block_size = 4096
 
        max_index = -1
        max_value = -1
        min_index = -1
        min_value = 1
 
        if end_seek > self.frames:
            end_seek = self.frames
 
        if block_size > end_seek - start_seek:
            block_size = end_seek - start_seek
 
        if block_size <= 1:
            samples = self.read(start_seek, 1)
            return samples[0], samples[0]
        elif block_size == 2:
            samples = self.read(start_seek, True)
            return samples[0], samples[1]
 
        for i in range(start_seek, end_seek, block_size):
            samples = self.read(i, block_size)
 
            local_max_index = numpy.argmax(samples)
            local_max_value = samples[local_max_index]
 
            if local_max_value > max_value:
                max_value = local_max_value
                max_index = local_max_index
 
            local_min_index = numpy.argmin(samples)
            local_min_value = samples[local_min_index]
 
            if local_min_value < min_value:
                min_value = local_min_value
                min_index = local_min_index
 
        return (min_value, max_value) if min_index < max_index else (max_value, min_value)
 
#not relevant to visualization
def interpolate_colors(colors, flat=False, num_colors=256):
    """ given a list of colors, create a larger list of colors interpolating
    the first one. If flatten is True a list of numers will be returned. If
    False, a list of (r,g,b) tuples. num_colors is the number of colors wanted
    in the final list """
 
    palette = []
 
    for i in range(num_colors):
        index = (i * (len(colors) - 1))/(num_colors - 1.0)
        index_int = int(index)
        alpha = index - float(index_int)
 
        if alpha > 0:
            r = (1.0 - alpha) * colors[index_int][0] + alpha * colors[index_int + 1][0]
            g = (1.0 - alpha) * colors[index_int][1] + alpha * colors[index_int + 1][1]
            b = (1.0 - alpha) * colors[index_int][2] + alpha * colors[index_int + 1][2]
        else:
            r = (1.0 - alpha) * colors[index_int][0]
            g = (1.0 - alpha) * colors[index_int][1]
            b = (1.0 - alpha) * colors[index_int][2]
 
        if flat:
            palette.extend((int(r), int(g), int(b)))
        else:
            palette.append((int(r), int(g), int(b)))
 
    return palette
 
class WaveformImage(object):
    def __init__(self, image_width, image_height, palette):
        self.image = Image.new("RGB", (image_width, image_height))
 
        self.image_width = image_width
        self.image_height = image_height
 
        self.draw = ImageDraw.Draw(self.image)
        self.previous_x, self.previous_y = None, None
 
        if palette==2:
	        colors = [
	                    (255,255,255),
	                    (255,255,255),
	                    (255,255,255),
	                    (225,248,255),
	                    (210,241,255),
	                    (195,232,255),
	                    (180,221,255),
	                    (165,208,255),
	                    (150,193,255),
	                    (135,175,255),
	                    (120,156,255),
	                    (105,134,255),
	                    (90,110,255),
	                    (75,85,255),
	                    (63,60,255),
	                    (64,45,255),
	                    (66,30,255),
	                    (76,0,255),
	                    (0,128,13),
	                    (8,138,0),
	                    (20,143,0),
	                    (33,148,0),
	                    (46,153,0),
	                    (60,158,0),
	                    (91,168,0),
	                    (108,173,0),
	                    (125,179,0),
	                    (143,184,0),
	                    (162,189,0),
	                    (182,194,0),
	                    (199,195,0),
	                    (204,184,0),
	                    (255,230,128),
	                    (255,221,119),
	                    (255,213,111),
	                    (255,203,102),
	                    (255,193,94),
	                    (255,181,85),
	                    (255,169,77),
	                    (255,157,68),
	                    (255,143,60),
	                    (255,129,51),
	                    (255,113,43),
	                    (255,97,34),
	                    (255,81,25),
	                    (255,63,17),
	                    (255,45,8),
	                    (255,26,0)
	                 ]
        elif palette==1:
	        colors = [
	                    (0, 0, 0),
	                    (58/4,68/4,65/4),
	                    (80/2,100/2,153/2),
	                    (90,180,100),
	                    (224,224,44),
	                    (255,60,30),
	                    (255,255,255)
	                 ]
 
        # this line gets the old "screaming" colors back...
        # colors = [self.color_from_value(value/29.0) for value in range(0,30)]
 
        self.color_lookup = interpolate_colors(colors)
        self.pix = self.image.load()
 
    def color_from_value(self, value):
        """ given a value between 0 and 1, return an (r,g,b) tuple """
 
        return ImageColor.getrgb("hsl(%d,%d%%,%d%%)" % (int( (1.0 - value) * 360 ), 80, 50))
 
    def draw_peaks(self, x, peaks, spectral_centroid):
        """ draw 2 peaks at x using the spectral_centroid for color """
 
        y1 = self.image_height * 0.5 - peaks[0] * (self.image_height - 4) * 0.5
        y2 = self.image_height * 0.5 - peaks[1] * (self.image_height - 4) * 0.5
 
        line_color = self.color_lookup[int(spectral_centroid*255.0)]
 
        if self.previous_y != None:
            self.draw.line([self.previous_x, self.previous_y, x, y1, x, y2], line_color)
        else:
            self.draw.line([x, y1, x, y2], line_color)
 
        self.previous_x, self.previous_y = x, y2
 
        self.draw_anti_aliased_pixels(x, y1, y2, line_color)
 
    def draw_anti_aliased_pixels(self, x, y1, y2, color):
        """ vertical anti-aliasing at y1 and y2 """
 
        y_max = max(y1, y2)
        y_max_int = int(y_max)
        alpha = y_max - y_max_int
 
        if alpha > 0.0 and alpha < 1.0 and y_max_int + 1 < self.image_height:
            current_pix = self.pix[x, y_max_int + 1]
 
            r = int((1-alpha)*current_pix[0] + alpha*color[0])
            g = int((1-alpha)*current_pix[1] + alpha*color[1])
            b = int((1-alpha)*current_pix[2] + alpha*color[2])
 
            self.pix[x, y_max_int + 1] = (r,g,b)
 
        y_min = min(y1, y2)
        y_min_int = int(y_min)
        alpha = 1.0 - (y_min - y_min_int)
 
        if alpha > 0.0 and alpha < 1.0 and y_min_int - 1 >= 0:
            current_pix = self.pix[x, y_min_int - 1]
 
            r = int((1-alpha)*current_pix[0] + alpha*color[0])
            g = int((1-alpha)*current_pix[1] + alpha*color[1])
            b = int((1-alpha)*current_pix[2] + alpha*color[2])
 
            self.pix[x, y_min_int - 1] = (r,g,b)
 
    def save(self, filename):
        # draw a zero "zero" line
        a = 25
        for x in range(self.image_width):
            self.pix[x, self.image_height/2] = tuple(map(lambda p: p+a, self.pix[x, self.image_height/2]))
 
        self.image.save(filename)
 
 
class SpectrogramImage(object):
    def __init__(self, image_width, image_height, fft_size, f_max, f_min, nyquist_freq, palette):
        self.image = Image.new("P", (image_height, image_width))
 
        self.image_width = image_width
        self.image_height = image_height
        self.fft_size = fft_size
        self.f_max = f_max
        self.f_min = f_min
        self.nyquist_freq = nyquist_freq
        self.palette = palette
 
        if nyquist_freq<f_max:
            print "\nWarning: The specified maximum frequency to draw (%d Hz) is higher that what the digital file allows, which is %d Hz. The image file will have black areas on top that correspond to empty data.\n" % (f_max,nyquist_freq)

        if palette==2:
	        colors = [
	                    (255,255,255),
	                    (255,255,255),
	                    (255,255,255),
	                    (225,248,255),
	                    (210,241,255),
	                    (195,232,255),
	                    (180,221,255),
	                    (165,208,255),
	                    (150,193,255),
	                    (135,175,255),
	                    (120,156,255),
	                    (105,134,255),
	                    (90,110,255),
	                    (75,85,255),
	                    (63,60,255),
	                    (64,45,255),
	                    (66,30,255),
	                    (76,0,255),
	                    (0,128,13),
	                    (8,138,0),
	                    (20,143,0),
	                    (33,148,0),
	                    (46,153,0),
	                    (60,158,0),
	                    (91,168,0),
	                    (108,173,0),
	                    (125,179,0),
	                    (143,184,0),
	                    (162,189,0),
	                    (182,194,0),
	                    (199,195,0),
	                    (204,184,0),
	                    (255,230,128),
	                    (255,221,119),
	                    (255,213,111),
	                    (255,203,102),
	                    (255,193,94),
	                    (255,181,85),
	                    (255,169,77),
	                    (255,157,68),
	                    (255,143,60),
	                    (255,129,51),
	                    (255,113,43),
	                    (255,97,34),
	                    (255,81,25),
	                    (255,63,17),
	                    (255,45,8),
	                    (255,26,0)
	                 ]
        elif palette==1:
	        colors = [
	                    (0, 0, 0),
	                    (58/4,68/4,65/4),
	                    (80/2,100/2,153/2),
	                    (90,180,100),
	                    (224,224,44),
	                    (255,60,30),
	                    (255,255,255)
	                 ]
 
        self.image.putpalette(interpolate_colors(colors, True))
 
        # generate the lookup which translates y-coordinate to fft-bin
        self.y_to_bin = []
        y_min = math.log10(f_min)
        y_max = math.log10(f_max)
        for y in range(self.image_height):
#            log scale
#            freq = math.pow(10.0, y_min + y / (image_height - 1.0) *(y_max - y_min))
#            arithmetic scale
            freq = f_min + y / (image_height - 1.0) *(f_max - f_min)
#            uses the nyquist frequency to allow files of different sampling rate
            bin = freq / nyquist_freq * (self.fft_size/2 + 1)
#            bin = freq / 22050.0 * (self.fft_size/2 + 1)
 
            if bin < self.fft_size/2:
                alpha = bin - int(bin)
 
                self.y_to_bin.append((int(bin), alpha * 255))
 
        # this is a bit strange, but using image.load()[x,y] = ... is
        # a lot slower than using image.putadata and then rotating the image
        # so we store all the pixels in an array and then create the image when saving
        self.pixels = []
 
    def draw_spectrum(self, x, spectrum):
        for (index, alpha) in self.y_to_bin:
            self.pixels.append( int( ((255.0-alpha) * spectrum[index] + alpha * spectrum[index + 1] )) )
 
        for y in range(len(self.y_to_bin), self.image_height):
            self.pixels.append(0)
 
    def save(self, filename):
        self.image.putdata(self.pixels)
        self.image.transpose(Image.ROTATE_90).save(filename)
 
 
def create_png(input_filename, output_filename_w, output_filename_s, image_width, image_height, fft_size, f_max, f_min, wavefile, palette, channel):
    """
    Given command line arguments this basically does everything.

    WHAT I HAVE GATHERED:
    db_spectrum has the frequencies of the sound file.
    spectral_centroid tells us what the color of the sound is.
    peaks tell us what the amplitude of the sound is.

    Should be trivial to adapt this from image output to output
    to our JavaScript visualizer now.
    """
    
    print "processing file %s:\n\t" % input_file,
 
    audio_file = audiolab.sndfile(input_filename, 'read')  #opens the wavfile; audio_file is an object now
 
    samples_per_pixel = audio_file.get_nframes() / float(image_width)
    nyquist_freq = (audio_file.get_samplerate() / 2) + 0.0
    """
    Initializes AudioProcessor class, which does FFT analysis and spits 
    out amplitudes and frequencies to the SpectrogramImage and WaveformImage 
    classes below later. For a stereo wav file, this selects a single channel 
    to analyze. We might want to analyze both channels to give more input to
    the visualizer,though.
    """
    processor = AudioProcessor(audio_file, fft_size, channel, numpy.hanning)
 
    if wavefile==1:
        waveform = WaveformImage(image_width, image_height, palette)
    spectrogram = SpectrogramImage(image_width, image_height, fft_size, f_max, f_min, nyquist_freq, palette)
 
    for x in range(image_width):
        #shows progress
        if x % (image_width/10) == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
 
        seek_point = int(x * samples_per_pixel)
        next_seek_point = int((x + 1) * samples_per_pixel)
        
        (spectral_centroid, db_spectrum) = processor.spectral_centroid(seek_point)
        
        #let's have a look at the spectral centroid and the db_spectrum
        #print "Spectral Centroid:" + str(spectral_centroid)
        #print "DB Spectrum:" + str(db_spectrum)
        
        if wavefile==1:
            #aha! The peaks and spectral centroid make up the waveform.
            #Since the spectral centroid indicates timbre (often referred to as color),
            #it's probably what colors the waveform.
            peaks = processor.peaks(seek_point, next_seek_point)
            #let's have a look at these peaks
            #print "Peaks:" + str(peaks)
            waveform.draw_peaks(x, peaks, spectral_centroid)
 
        spectrogram.draw_spectrum(x, db_spectrum)
 
    if wavefile==1:
        waveform.save(output_filename_w)
    spectrogram.save(output_filename_s)
 
    print " done"


def processWav(filename, channel):
    """
    filename: path to a wav file
    Channel: 1 for left, 2 for right
    Returns centroids, frequencies, volumes
    """
    #open file
    audio_file = audiolab.sndfile(filename, 'read')
    #should be length of audiofile in seconds * 60. will fix this later
    import contextlib
    import wave
    with contextlib.closing(wave.open(filename, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    duration *= 60 #60 data points for every second of audio yay
    duration = int(duration) #can only return an integer number of frames so yeah
    #print duration
    #Not really samples per pixel but I'll let that slide
    samples_per_pixel = audio_file.get_nframes() / float(duration)
    #some rule says this frequency has to be half of the sample rate
    nyquist_freq = (audio_file.get_samplerate() / 2) + 0.0
    #fft_size stays 4096
    processor = AudioProcessor(audio_file, 4096, channel, numpy.hanning)
    
    centroids = []
    frequencies = []
    volumes = []

    for x in range(duration):
        seek_point = int(x * samples_per_pixel)
        next_seek_point = int((x + 1) * samples_per_pixel)
        (spectral_centroid, db_spectrum) = processor.spectral_centroid(seek_point)
        peaks = processor.peaks(seek_point, next_seek_point)
        
        centroids.append(spectral_centroid)
        frequencies.append(db_spectrum)
        volumes.append(peaks)
    #print "Centroids:" + str(centroids)
    #print "Frequencies:" + str(frequencies)
    #print "Volumes:" + str(volumes)
    
    #convert volumes[] from peaks to actual volumes
    for i in range(len(volumes)):
        volumes[i] = abs(volumes[i][0]) + abs(volumes[i][1])

    return centroids, frequencies, volumes

 
if __name__ == '__main__':
    #note: optparse is deprecated
    parser = optparse.OptionParser("usage: %prog [options] input-filename", conflict_handler="resolve")
    parser.add_option("-a", "--waveout", action="store", dest="output_filename_w", type="string", help="output waveform image (default input filename + _w.png)")
    parser.add_option("-o", "--wavefile", action="store", dest="wavefile", type="int", help="draw waveform image (yes:1, no: 0; default: no)")
    parser.add_option("-s", "--specout", action="store", dest="output_filename_s", type="string", help="output spectrogram image (default input filename + _s.png)")
    parser.add_option("-w", "--width", action="store", dest="image_width", type="int", help="image width in pixels (default %default)")
    parser.add_option("-h", "--height", action="store", dest="image_height", type="int", help="image height in pixels (default %default)")
    parser.add_option("-f", "--fft", action="store", dest="fft_size", type="int", help="fft size, power of 2 for increased performance (default %default)")
    parser.add_option("-m", "--fmax", action="store", dest="f_max", type="int", help="Maximum freq to draw, in Hz (default %default)")
    parser.add_option("-i", "--fmin", action="store", dest="f_min", type="int", help="Minimum freq to draw, in Hz (default %default)")
    parser.add_option("-p", "--palette", action="store", dest="palette", type="int", help="Which color palette to use to draw the spectrogram, 1 for color and 2 for black on white (default %default)")
    parser.add_option("-c", "--channel", action="store", dest="channel", type="int", help="Which channel to draw in a stereo file, 1 for left or 2 for right (default %default)")
    parser.add_option("-v", "--version", action="store_true", dest="version", help="display version information")
 
    parser.set_defaults(output_filename_w=None, output_filename_s=None, image_width=500, image_height=170, fft_size=2048, f_max=22050, f_min=10, wavefile=0, palette=1, channel=1)
    
    (options, args) = parser.parse_args()
 
    if not options.version:
	    if len(args) == 0:
	        parser.print_help()
	        parser.error("not enough arguments")
 
	    if len(args) > 1 and (options.output_filename_w != None or options.output_filename_s != None):
	        parser.error("when processing multiple files you can't define the output filename!")
 
	    # process all files so the user can use wildcards like *.wav
	    for input_file in args:
	        if options.channel==2:
	            output_file_w = options.output_filename_w or input_file + "_w_r.png"
	            output_file_s = options.output_filename_s or input_file + "_s_r.png"
	        else:
	            output_file_w = options.output_filename_w or input_file + "_w.png"
	            output_file_s = options.output_filename_s or input_file + "_s.png"
 
	        args = (input_file, output_file_w, output_file_s, options.image_width, options.image_height, options.fft_size, options.f_max, options.f_min, options.wavefile, options.palette, options.channel)
 
            #bam. work backwards from create_png in order to figure out how this program works`
	    create_png(*args)
    else:
        print "\n svt version 0.4"

