# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import soundfile
import shutil
import os

from google_search import *
from speak import *
from youtube import *
from chatbot import *
from authentication import *


def run():
    if os.path.exists('audio_file'):
        shutil.rmtree(r'audio_file')
    os.mkdir('audio_file')
    freq = 44100
    duration = 5
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=1)
    sd.wait()
    write("audio_file/recording0.wav", freq, recording)


    data, samplerate = soundfile.read('audio_file/recording0.wav')
    soundfile.write('audio_file/recording1.wav', data, samplerate, subtype='PCM_16')


    r = sr.Recognizer()

    with sr.AudioFile("audio_file/recording1.wav") as source:
        audio = r.record(source)
        try:
            s = r.recognize_google(audio)
            print("Text: "+s)
        except Exception as e:
            # print("Exception: "+str(e))
            run()

    # text = google_search(query = s)
    # speaking(text)
    if(s!=""):
        if((s == 'What is your name ') or (s == 'who are you')):
            speaking('I am Friday Your personal AI')
        if("exit" in s):
            speaking('Good Bye Sir')
            shutil.rmtree(r'audio_file')
        if("play" in s):
            query = str(s)
            query = query.replace(' ','')
            query = query.replace('play','')
            query = query.replace('youtube','')
            
            youtube(query)
        else:
            speaking(chatbot(s))
            run()
    else:
        run()

def auth():
    for i in range(3):
        flg = authentication()
        if(flg == True):
            return True
    
    return False

flg = auth()

if flg == True:
    speaking(" Welcome Back Sir ")
    run()
        

    
