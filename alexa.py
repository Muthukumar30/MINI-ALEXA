import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia

listener=sr.Recognizer()
engine=pyttsx3.init()
#voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("hi i am your alexa listening to your command")
            talk('hi i am your alexa listening to your command')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime(%I:%M %p)
        talk('current time is',time)
        print('current time is',time)
    elif 'tell me about' in command:
        content=command.replace('tell me about','')
        info=wikipedia.summary(content,1)
        print(info)
        takl(info)
    elif 'joke' in command:
        joke=pyjokes.get_jokes()
        print(jokes)
        talk(joke)
    else:
        talk("sorry   i don't understand you")
while true:
    run_alexa()
























