# Audio-Profanity-Filter
Filter out profanity/foul words from the audio along with retain the quality of an audio.

# PROBLEM TACKLED-
1. No audio censorship for game streaming.
2. Podcasts and the list goes on …...
3. Requires all sorts of manual audio censorships which actually is time consuming.

# Solution-
1.NLP based profanity filtering 
2. Via Google Cloud Speech To Text, we are detecting timestamps of foul words and then removing them while retaining the person's audio quality. 
3. We make use of audio processing techniques to beep out the foul words thus retaining sound quality of person.


TECH STACK-----
    
   1. Google Cloud Speech To Text in Python.
   
   2. Audio Pre-Processing in Python PyAudio, ffmpeg and PyDub.
   
   Valuability in various fields------
   All the entertainment based industries that make use of audio streaming that is almost all of them. Like :
  1.Podcasts & Youtube Online
  2.Gaming---Adding Child Filters.
  4.Media----Detecting foul words in live broadcasting.
  6.Censorship of Movies----Censorship of audio content in movies
  8.Language Support----Supports  as many languages as supported by Google.
  
  
  
 # Content---
  
#  beep.py 
This is used to generate a signal generating the intermediate beep sound wave.
#  final_file.py
It is the final version whose input file is an audio wile in 'Flac' format and can be cloned into the system.
# joining_wav.py 
This is used to combine different moduled wav format audio files.
# a4.py
It is a real time audio profanity filtered text display.

# WORKFLOW--
https://docs.google.com/presentation/d/1Y8NCyaMk95sFkZvT9qCwDk_4J9fCzFTISMkFBMRuFF0/edit#slide=id.g7c9cb13d1a_0_22

# How to run the code- 

In command prompt type "python final_file.py"


Drop --comments-- if found any issues:)
