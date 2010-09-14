#! /usr/bin/env python

import sys
import os
from numpy import *
from scipy import *
import scikits.audiolab as audiolab
import matplotlib.pylab as plt

project_path = sys.argv[1]  # where the audio files are
recording_number = int(sys.argv[2]) # e.g. 9, for #09

pixclock_prefix = "PixClock "
velocity_threshold = 0.025

positive_transitions = []
negative_transitions = []

def reduce_runs(l):
    last = -2
    out = []
    for i in l:
        if i != last + 1:
            out.append(i)
        last = i
    return out    

for c in range(0,4):

    filepath = os.path.join(project_path, "%s%d#%.2d.wav" % (pixclock_prefix, c+1, recording_number))

    print(filepath)

    (wav_data, rate, format) = audiolab.wavread(filepath)

    wav_velocity = diff(wav_data)
    smooth_wav_velocity = convolve(wav_velocity, ones((100)))

    plt.plot(smooth_wav_velocity[0:-1:100])
    plt.show()

    print max(smooth_wav_velocity)
    print min(smooth_wav_velocity)

    positive_transitions.append(reduce_runs(where(smooth_wav_velocity > velocity_threshold)[0]))
    negative_transitions.append(reduce_runs(where(smooth_wav_velocity < -velocity_threshold)[0]))


    print("n items = %d" % (len(positive_transitions[-1])))

plt.figure()
plt.hold(True)

print(positive_transitions)

for c in range(0,len(positive_transitions)):
    for t in positive_transitions[c]:
        print("%d,%d +" % (c,t))
        plt.plot(c, t, '+')
    
    for t in negative_transitions[c]:
        plt.plot(c, t, 'o')

print positive_transitions
    
plt.show()


