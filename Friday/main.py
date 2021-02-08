import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
#Pyaudio - pip install pyaudio

print("Initializing FRIDAY")

prefix = "Sir" #Yourname

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronouce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will with you as per the currect time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + prefix) 

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + prefix)

    else:
        speak("Good Evening" + prefix)
    speak("I am Friday., the successor to JARVIS. How may I help you?")    

#This function will take command from the microphoe
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recongnizing...")
        query = r.Recognize_google(audio, Language = 'en-GB')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Sorry {prefix}, please say that again")
        query = None
    return query

def sendemail(to, content):
    server = smtplib.smtp('smtp.gmail.com', 587)
    server.eclo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.send('toemail@gmail.com', to, content)
    server.close()
#Main program starts here...
def Main()
    speak("Initializing protocol.. FRIDAY.....")
    wishMe()
    query = takeCommand()

    #Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('Scanning wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences =3 )
        print(results)
        speak(results)

    elif 'open youtube' in query.lower:
        url = "youtube.com"
        firefox_path = 'C:\Program Files\Mozilla Firefox\firefox.exe %s'
        webbrowser.get(firefox_path).open(url)

    elif 'open google' in query.lower:
        url = "google.com"
        firefox_path = 'C:\Program Files\Mozilla Firefox\firefox.exe %s'
        webbrowser.get(firefox_path).open(url)

    elif 'play music' in query.lower():
        songs = os.listdir("")
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0])

    elif 'the time' in query.lower
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{prefix} the time is {strftime}")

    elif 'open visual studios' in query.lower
        codepath = "D:\\Users\\Sweed\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'email to [Senders email/name]' in query.lower():
        try:
            speak("What should I send? sir")
            content = takeCommand()
            to = "email"
            sendemail(to, content)
            speak('Accessing provided servers. Writting email. Finishing up. Sent.')
        except Exception as e:
            print(e)
        

