# Audio-Profanity-Filter
Filter out profanity/foul words from the audio along with retain the quality of an audio.

# PROBLEM-
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
  
# File with name beep.py is used to generate a signal generating the intermediate beep sound wave.
# File with name final_file.py is the final version whose input file is an audio wile in 'Flac' format and can be cloned into the system.
# File with name combined_wav.py is used to combine different moduled wav format audio files.
# File with name a4.py is a real time audio profanity filtered text display.



How to run the code- 
In command prompt type "python final_file.py"


Drop --comments-- if found any issues:)
