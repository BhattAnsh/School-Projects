from logging import setLoggerClass
import os
import sys
import speech_recognition as sr
import pyttsx3
import pyaudio
import cv2
import datetime
import requests
import pywhatkit
import random
from bs4 import BeautifulSoup
import webbrowser
import wikipedia
import pyscreenshot
# ----------------------------------------------------------------------------------------------------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 175)
# ----------------------------------------------------------------------------------------------------------------
def takecommand():
#friday will take command from here
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listning...')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing....')
        text = r.recognize_google(audio, language='en-IN')
        print(text)
    except Exception as e:
        print('')
        return "None"
    return text

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# -----------------------------------------------------------------------------------------------------------------
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak('good morning sir')
    elif 12 <= hour <= 18:
        speak('good afternoon sir')
    else:
        speak('good evening sir')
# -----------------------------------------------------------------------------------------------------------------
def taskexecution():
    wish()
    while True:
        def byy():
            hour = int(datetime.datetime.now().hour)#this will return the time in hour
            if 21<=hour<=6:
                speak('good night sir. Take care. Thanks for using me.')
                sys.exit()
            else:
                speak('Bye sir just take my name when ever you need me.')
                sys.exit()
# ---------------------------------------------------------------------------------------------------------------
        def speak(audio):
            engine.say(audio)
            engine.runAndWait()

        def youtube(text):
            pywhatkit.playonyt(text)

        def search():
            text2 = text.replace('search' and 'friday', '')
            speak('searching' + text2)
            pywhatkit.search(text2)

        def songs():
            choice = random.choice(choices)
            speak('playing' + choice)
            pywhatkit.playonyt(choice)

        def time():
            time = datetime.datetime.now().strftime('%H %M %p')
            speak(f'time is{time}')

        text = takecommand().lower()
        if text == 'hello friday' or text == 'hi friday' or text == 'hey friday':
            wish()
            speak("I am friday how can I help you sir")
# ----------------------------------------------------------------------------------------------------------------
        elif text == 'friday open chrome' or text == 'open chrome' or text == 'friday please open the chrome' or text == "please open the chrome" or text == 'friday can you open the chrome' or text == 'can you open the chrome':
            cpath= "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak('opening chrome')
            os.startfile(cpath)
# ----------------------------------------------------------------------------------------------------------------
        elif 'search' in text:
            search()
# ----------------------------------------------------------------------------------------------------------------
        elif text == 'friday open pycharm' or text == 'open pycharm' or text == 'can you open the pycharm' or  text == 'friday can you open pycharm ' or text == 'friday pycharm' or text == 'pycharm':
            ppath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe"
            speak('opening pycharm')
            os.startfile(ppath)
# ----------------------------------------------------------------------------------------------------------------
        elif text == 'open microsoft edge' or text == 'friday open microsoft edge' or  text == 'open microsoft' or text == 'friday open microsoft' or text == 'can you open microsoft' or text == 'friday can you open microsoft':
            mpath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            speak('opening Microsoft edge')
            os.startfile(mpath)
# ----------------------------------------------------------------------------------------------------------------
        elif text == 'open youtube' or text == 'friday open youtube' or text == 'open the youtube' or text == 'friday open the youtube' or text == 'can you open youtube' or text == 'friday can you open youtube':
            webbrowser.open('www.youtube.com')
            speak('opening youtube')
# ----------------------------------------------------------------------------------------------------------------
        elif text == 'open spotify' or text == 'friday open spotify' or  text == 'open the spotify' or text == 'friday open the spotify' or text == 'can you open the spotify' or text == 'friday can you open the spotify':
            webbrowser.open('open.spotify.com')
            speak('opening spotify')
# ----------------------------------------------------------------------------------------------------------------
        elif text == 'open whatsapp' or text == 'friday open whatsapp' or text == 'can you open whatsapp' or text == 'friday can you open whatsapp' or text == 'open the whatsapp' or text == 'friday open the whatsapp':
            webbrowser.open('web.whatsapp.com')
            speak('opening whatsapp')
# ----------------------------------------------------------------------------------------------------------------
        elif text == 'play song' or text == 'friday play song' or text == 'play some song' or text == 'friday play some song' or text == 'song' or text == 'can you play song' or text == 'friday can you play song':
            choices = ['quafirana', 'jab koi baat Atif Aslam', 'khairiyat', 'shayad', 'agar tum saath ho',
                               'tu hi yaar mera', 'kalank', 'ek tarfa', 'asal me', 'Baarish lete aana', 'likhe jo khat tujhe by sanam',
                               'ye raatein ye mausam by sanam']
            songs()
# ---------------------------------------------------------------------------------------------------------------
        elif 'shopping' in text:
            webbrowser.open('www.amazon.in')
            speak('sir I am opening amazon so you can shop whatever you want')
# ---------------------------------------------------------------------------------------------------------------
        elif 'who is' in text:
            text2 = text.replace("friday" and 'can you tell me', '')
            print(wikipedia.summary(text2, sentences=2))
            speak('according to wikipedia')
            speak(wikipedia.summary(text2, sentences=2))
# ---------------------------------------------------------------------------------------------------------------
        elif 'close microsoft' in text:
            speak('closing microsoft edge')
            os.system("taskkill /f /im msedge.exe")
        elif 'close chrome' in text:
                speak('closing chrome')
                os.system("taskkill /f /im chrome.exe")
        elif 'close youtube' in text:
                speak('closing youtube')
                os.system("taskkill /f /im chrome.exe")
        elif 'close spotify' in text:
            speak('closing spotify')
            os.system("taskkill /f /im msedge.exe")
# ---------------------------------------------------------------------------------------------------------------
        elif 'turn off' in text:
            speak('you can press on power button to turn off your computer')
# ---------------------------------------------------------------------------------------------------------------
        elif 'screenshot' in text:
            speak('taking screenshot')
            image = pyscreenshot.grab()
            image.show()
            image.save('ansh.png')
# ---------------------------------------------------------------------------------------------------------------
        elif text == 'i love you' or text == 'i love you friday':
            speak('i love you to sir.')
        elif text == 'can you sing' or text == 'sing' or text == 'can you sing a song':
            speak("no i can not sing any song but i can play song")
            speak('should i play a song')
        elif text == 'thank you friday' or text == 'thank you':
            speak('my pleasure sir')
        elif text == 'who are you' or text == 'who are you friday' or text == 'tell us something about you' or text == 'friday give introduction about you':
            speak('I am an AI which is created by Ansh Bhatt I can help you in making your life easier. And I keep learning from mistake I will try to do my best while helping you.')
        elif 'name' in text:
            speak('Ansh Bhatt')
        elif 'whistle' in text:
            speak('yeah ofcourse I am waiting for this')
            os.startfile("C:\\Users\\Ansh Bhatt\\Downloads\\wishtel.mp3")
        elif 'clap' in text:
            os.startfile("C:\\Users\\Ansh Bhatt\\Downloads\\mixkit-conference-audience-clapping-strongly-476.wav")
        elif 'fart' in text:
            os.startfile("C:\\Users\\Ansh Bhatt\\Downloads\\fart-01.mp3")
        elif 'how are you' in text:
            speak('I am good sir. What about you?')
        elif 'fine' in text:
            speak("that's great! sir tell me how can i help you?")
        elif 'search' in text:
            search()
        elif 'tell me my location' in text:
            speak('I am not sure but I think you are currently somewhere in New Delhi')
# ------------------------------------------------------------------------------------------------------------------
        elif text == 'can you search on amazon' or text == 'search on amazon' or text == 'i want to search on amazon' or text == 'open amazon':
            speak('sir tell me what should I search on the amazon.')
            while True:
                text2 = takecommand().lower
                if True:
                    speak('searching on amazone')
                    webbrowser.open("https://www.amazon.in/s?k="+text2)
                else:
                    print()
# -------------------------------------------------------------------------------------------------------------
        elif 'youtube' in text:
            t = text.replace('play on youtube', '')
            speak('ok sir playing on youtube.')
            youtube(t)
# ------------------------------------------------------------------------------------------------------------------
        elif 'time' in text:
            time()
# -------------------------------------------------------------------------------------------------------------
        elif 'show my location' in text or 'show my current location' in text or 'show me where I am right now' in text:
            webbrowser.open('https://www.google.com/maps/place/BLOCK-95,+CENTRAL+GOVT.+RESIDENTIAL+COMPLEX,+DIZ+Staff+Quarters,+Connaught+Place,+New+Delhi,+Delhi+110001/@28.6290781,77.2098285,54m/data=!3m1!1e3!4m5!3m4!1s0x390cfd4e9a83952f:0x4129389a04c133b3!8m2!3d28.6290686!4d77.2097746')

# --------------------------------------------------------------------------------------------------------------
        elif 'temperature' in text:
            try:
                search = text
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                tempereature = data.find('div', class_="BNeawe").text
                print(f"current temperature is {tempereature}")
                speak(f"current temperature is {tempereature}")
            except:
                speak('Sorry sir due to internet error I am not able to find the temperature.')
# --------------------------------------------------------------------------------------------------------------
        elif "covid" in text:
            url = "https://news.google.com/covid19/map?hl=en-IN&mid=%2Fm%2F09f07&gl=IN&ceid=IN%3Aen"
            r = requests.get(url)
            htmlcontent = r.text
            soup = BeautifulSoup(r.text, 'html.parser')
            div = soup.find(class_= "sgXwHf wdLSAe ROuVee")
            result = (list(div.strings))
            Name = result[0]
            Total_case = result[1]
            Today_case = result[2]
            Total_death = result[4]
            print("Total cases= "+Total_case)
            speak("Total cases in your city {Total_ca}")
            speak('During this pandemic you should stay safe sir.')
            print("Cases came in last 24hrs= "+Today_case)
            print("Total deaths= "+Total_death)
# --------------------------------------------------------------------------------------------------------------
        elif 'goodbye' in text or 'bye' in text:
            byy()
        elif 'sleep' in text or 'take rest' in text:
            break
        else:
            print("")
# ---------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    while True:
        permission = takecommand().lower()
        if "friday" in permission:
            taskexecution()
        elif 'friday' in permission:
            taskexecution()
        elif "exit" in permission:
            sys.exit()
