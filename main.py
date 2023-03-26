import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listerer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listerer.listen(source)
            command = listerer.recognize_google(voice)
            if "may" in command:
                command = command.replace("may", "")
                print(command)

    except:
        pass
    
    return command

def run_may():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is "+ time)

    elif "who is" in command:
        person = command.replace("who is", "")
        info1 = wikipedia.summary(person, 3)
        print(info1)
        talk(info1)

    elif "what is" in command:
        subject = command.replace("what is", "")
        info2 = wikipedia.summary(subject, 3)
        print(info2)
        talk(info2)

    elif "date" in command:
        talk("Sorry, I have a headache")
        
    elif "are you single" in command:
        talk("I am in a relationship with wifi")

    elif "joke" in command:
        joke = talk(pyjokes.get_joke())

    else:
        talk("Please say again...")


run_may()
