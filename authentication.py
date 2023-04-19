from speak import *
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import soundfile
import shutil
import os

def authentication():
    flg = False
    
    if os.path.exists('password'):
        shutil.rmtree(r'password')
    os.mkdir('password')
    freq = 44100
    duration = 5
    speaking(" What is Your Password ? ")
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=1)
    sd.wait()
    write("password/pass.wav", freq, recording)


    data, samplerate = soundfile.read('password/pass.wav')
    soundfile.write('password/pass1.wav', data, samplerate, subtype='PCM_16')
    r = sr.Recognizer()

    with sr.AudioFile("password/pass1.wav") as source:
        audio = r.record(source)
        try:
            
            s = r.recognize_google(audio)
            print(s)
        except Exception as e:
            pass
    if(str(s).lower()=="Hello Friday"):
        flg = True
        shutil.rmtree(r'password')
        
        
    return flg