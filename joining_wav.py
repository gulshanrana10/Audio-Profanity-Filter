# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:00:45 2020

@author: Gulshan Rana
"""
'''
import audiolab
import scipy
#adding first half and the generated beep
a, fs, enc = audiolab.wavread('audio1.wav')
b, fs, enc = audiolab.wavread('beep.wav')
c = scipy.vstack((a,b))
audiolab.wavwrite(c, 'ab.wav', fs, enc)
#adding other half part
d, fs, enc = audiolab.wavread('ab.wav')
e, fs, enc = audiolab.wavread('ab.wav')

f = scipy.vstack((d,e))
audiolab.wavwrite(f, 'finaud1.wav', fs, enc)'''



from pydub import AudioSegment

sound1 = AudioSegment.from_wav("sound0.wav")
sound2 = AudioSegment.from_wav("beep.wav")

combined_sounds = sound1 + sound2
combined_sounds.export("finaud1.wav", format="wav")