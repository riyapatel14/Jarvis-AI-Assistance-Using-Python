import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import subprocess
import webbrowser as wb
import os
import random
from PIL import ImageGrab

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Jarvis at your service, How can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('21104141.riya.patel@gmail.com', 'password')
    server.sendmail('21104141.riya.patel@gmail.com', to, content)
    server.close()

def playMusic():
    music_dir = 'C:\\Users\\Riya Patel\\Music'  # Change this to your music directory
    songs = os.listdir(music_dir)
    song = random.choice(songs)
    os.startfile(os.path.join(music_dir, song))

def screenshot():
    img = ImageGrab.grab()
    save_path = r"C:\Users\Riya Patel\Downloads\Music\ss.png"
    # Ensure directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    img.save(save_path)
    speak("Screenshot taken")

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
                print(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There were multiple results for that query, please be more specific.")
                print(e.options)
            except wikipedia.exceptions.PageError:
                speak("I could not find any results for your query.")
            except Exception as e:
                speak("Sorry, I encountered an error while searching Wikipedia.")
                print(e)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'riyap140503@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif 'search in chrome' in query:
            speak("What should I search?")
            search = takeCommand().lower()
            url = f"https://{search}.com"
            try:
                chromepath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
                subprocess.Popen([chromepath, url])
            except Exception as e:
                print(f"Failed to open Chrome: {e}")
                speak("Unable to open Chrome, opening with default browser.")
                wb.open_new_tab(url)
        elif 'play music' in query:
            playMusic()
        elif 'take screenshot' in query:
            screenshot()
        elif 'offline' in query:
            speak("Going offline. Goodbye!")
            break
