#! /usr/bin/env python

import sys
from numpy import *
from scipy import *
import scikits.audiolab as audiolab
import matplotlib.pylab as plt

project_path = sys.argv[1]  # where the audio files are
recording_number = int(sys.argv[2]) # e.g. 9, for #09

pixclock_prefix = "PixClock "
velocity_threshold = 0.25

position_transitions = []
negative_transitions = []

for c in range(0,4):

    filepath = os.join(project_path, "%s%d #%.2d" % (pixclock_prefix, c, recording_number))

    print(filepath)

    (wav_data, rate, format) = audiolab.wavread(filepath)

    wav_velocity = diff(wav_data)
    smooth_wav_velocity = convolve(wav_velocity, ones((100)))

    positive_transitions[c] = where(smooth_wav_velocity > velocity_threshold)
    negative_transitions[c] = where(smooth_wav_velocity < -velocity_threshold)

plt.figure()
plt.hold(True)

for c in range(0,4):
    for t in position_transitions:
        plt.plot(c, t, '+')
    
    for t in negative_transitions:
        plt.plot(c, t, 'o')
        
    



