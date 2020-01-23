# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:21:14 2020

@author: Gulshan Rana
"""

import numpy as np
from scipy.io.wavfile import write
#Generating beep at 
sps = 44100
freq_hz = 1000.0
duration = 0.3
vol = 0.3

esm = np.arange(duration * sps)
wf = np.sin(2 * np.pi * esm * freq_hz / sps)
wf_quiet = wf * vol
wf_int = np.int16(wf_quiet * 32767)
write("beep.wav", sps, wf_int)


''' 
for combining audios--         ffmpeg -i xyz.wav -ss 0.1 -t 2.6 -acodec copy audio1.wav && ffmpeg 
                                      -i xyz.wav -ss 3.3 -t 6.7 -acodec copy audio2.wav '''

