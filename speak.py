import pyttsx3
engine = pyttsx3.init()

def speaking(text):


    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[7].id)
    engine.say(text)
    engine.runAndWait()


