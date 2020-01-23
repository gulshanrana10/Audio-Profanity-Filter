
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:00:49 2020

@author: Gulshan Rana
"""

from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import os
#import audiolab
import numpy as np
from scipy.io.wavfile import write
#from subprocess import call
from pydub import AudioSegment

def sample_recognize(local_file_path):
    
    client = speech_v1.SpeechClient.from_service_account_json('PrestiSolutions-fb3de2002b43.json')

    language_code = "en-IN"
    sample_rate_hertz = 48000
    enable_word_time_offsets = True
    profanity_filter= True
    
    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    
    config = {
        "enable_word_time_offsets": enable_word_time_offsets,
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "profanity_filter": profanity_filter
    }
    #reading the audio file
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content} # audio ready to be propcessed
    #recognising the profaned transcript
    response = client.recognize(config, audio)
        
    
    start_time=[]
    end_time=[] 
    timeline=[]       
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
        for word in alternative.words:
           timeline.append(word.start_time.seconds+word.start_time.nanos*(10**-9))
           timeline.append(word.end_time.seconds+word.end_time.nanos*(10**-9))
           if '*' in word.word:
               start_time.append(word.start_time.seconds+word.start_time.nanos*(10**-9))
               end_time.append(word.end_time.seconds+word.end_time.nanos*(10**-9))
    return start_time,end_time,timeline

input_audio='inaudio.aac'

os.system(('ffmpeg -i {} -vn out1.flac mono.wav ').format(input_audio))    #  for converting format
os.system('ffmpeg -i out1.flac -ac 1 mono.flac ')     #for creating single channel of audio
# ffmpeg -i xyz1.wav -ss 0 -t 3 -acodec copy sound0.wav
#audio_path="mono.wav"
print(1)
start_time,end_time,timeline= sample_recognize('mono.flac')
print(2)
#scr_tst.py()
    



#Generating beep at profanity 
sps = 44100
freq_hz = 1000.0
duration = 0.3
vol = 0.3
esm = np.arange(duration * sps)
wf = np.sin(2 * np.pi * esm * freq_hz / sps)
wf_quiet = wf * vol
wf_int = np.int16(wf_quiet * 32767)
write("beep.wav", sps, wf_int)


start_time,end_time
init_=0.0
len_=len(start_time)
def split_profaned_audio(audio_path,start_time,end_time,ti_me):
    audio_path==audio_path
    start_time=start_time
    end_time=end_time
    audio_file="audio"+str(ti_me+1)+".wav"
    audio_file = r"%s"%audio_file
    os.system(('ffmpeg -i {} -ss {} -t {} -acodec copy {}').format(audio_path,start_time,end_time-start_time,audio_file))
    print('done')
   
audio_path='mono.wav'    

print('split0 ok')

split_profaned_audio(audio_path,timeline[0]+0.1,start_time[0]+0.1,-1)   #initialisation
#call(["ffmpeg","-i", "xyz1.wav", "-ss", "0", "-t", "start_time[1]", "-acodec", "copy", "sound0.wav"])
#sound0 = open("audio0.flac", "rb").read()
#beep1 = open("beep.flac", "rb").read()
#combined_sounds = sound0 + beep1
#combined_sounds = open("combined_sounds.flac", "wb").write(combined_sounds)
sound = AudioSegment.from_wav("audio0.wav")
beep = AudioSegment.from_wav("beep.wav")
combined_sounds = sound + beep
combined_sounds.export("combined_sounds.wav", format="wav")


if len_!=1:
    for ti_me in range(len_-1):
        split_profaned_audio(audio_path,end_time[ti_me]+0.1,start_time[ti_me+1]+0.1,ti_me)   #initialisation
        #call(["ffmpeg","-i", "xyz1.wav", "-ss", "0", "-t", "start_time[1]", "-acodec", "copy", "sound0.wav"])
        #sound="audio"+str(ti_me+1)+".flac"
        #sound = r"%s"%sound
        #sound = open(sound, "rb").read()
        
        #sound = open("sound.flac", "wb").write(sound)
        #combined_sounds = combined_sounds+sound + beep1
        #combined_sounds = open("combined_sounds.flac", "wb").write(combined_sounds)
        #combined_sounds= open("combined_sounds.flac", "rb").read()
    for ti_me in range(len_-1):
        '''beep1 = open("beep.flac", "rb").read()
        sound="audio"+str(ti_me+1)+".flac"
        sound = r"%s"%sound
        sound = open(sound, "rb").read()
        sound1a=sound+beep1
        sound1 = open("sound1a.flac", "wb").write(sound1a)
        
        sound1 = open("sound1.flac", "rb").read()
        c1 = open(combined_sounds, "rb").read()
        combined_sounds=c1+sound1
        
        
        sound="audio"+str(ti_me+1)+".flac"
        input_audio = r"%s"%sound
        sound="audio"+str(ti_me+1)+".wav"
        output_audio = r"%s"%sound
        os.system(('ffmpeg -i {} -vn {} ').format(input_audio,output_audio))
        ''' 
        sound="audio"+str(ti_me+1)+".wav"
        input_audio = r"%s"%sound
        beep = AudioSegment.from_wav("beep.wav")
        sub_sound = AudioSegment.from_wav(input_audio)
        
        combined_sounds=combined_sounds+sub_sound+beep
        
    combined_sounds.export("combined_sounds.wav", format="wav")
        
    print('winner')
        
else: 
    ti_me=0
    split_profaned_audio(audio_path,end_time[ti_me]+0.1,timeline[-1]+0.1,ti_me)   #initialisation
    '''call(["ffmpeg","-i", "xyz1.wav", "-ss", "0", "-t", "start_time[1]", "-acodec", "copy", "sound0.wav"])
    sound="audio"+str(ti_me+1)+".flac"
    sound = r"%s"%sound
    sound = open(sound, "rb").read()
    sound = open("sound.flac", "wb").write(sound)
    combined_sounds = combined_sounds+sound + beep1
    combined_sounds = open("combined_sounds.flac", "wb").write(combined_sounds)
    combined_sounds= open("combined_sounds.flac", "rb").read()'''
    sound="audio"+str(ti_me+1)+".flac"
    input_audio = r"%s"%sound
    sub_sound = AudioSegment.from_wav("input_audio.wav")
        
    combined_sounds=combined_sounds+sub_sound+beep
        
    combined_sounds.export("combined_sounds.wav", format="wav")
    print('else_winner')


split_profaned_audio(audio_path,end_time[-1]+0.1,timeline[-1]+0.1,len_-1)
sound="audio"+str(len_)+".wav"
input_audio = r"%s"%sound
sub_sound = AudioSegment.from_wav(input_audio)

        
combined_sounds=combined_sounds+sub_sound
        
combined_sounds.export("combined_sounds.wav", format="wav")
'''
split_profaned_audio(audio_path,7.5,2.5,0)
sound1 = AudioSegment.from_wav("audio1.wav")
combined_sounds = combined_sounds + sound1 + beep
combined_sounds.export("finaudF0.0.wav", format="wav")
print('aok')



for ti_me in range(len_-1):
    split_profaned_audio(audio_path,start_time[ti_me+1],end_time[ti_me],ti_me+1)
    audio_file="audio"+str(ti_me+1)+".wav"
    audio_file = r"%s"%audio_file
    audio = AudioSegment.from_wav(audio_file)
    audio=audio+beep
    combined_sounds = combined_sounds +audio
    
combined_sounds = combined_sounds + beep
length_of_audio=timeline[-1]
split_profaned_audio(audio_path,end_time[-1],length_of_audio,len_)
audio1=AudioSegment.from_wav("{}").format("audio"+str(len_+1)+".wav")
combined_sounds=combined_sounds+audio1
combined_sounds.export("finaudF.0.wav", format="wav")

print(3)
    
    
'''


