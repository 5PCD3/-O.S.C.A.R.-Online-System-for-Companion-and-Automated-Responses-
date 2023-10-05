# O.S.C.A.R. (Online System for Companion and Automated Responses)
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import requests
from bs4 import BeautifulSoup
import pyautogui
import time
#import spotipy
#from spotipy.oauth2 import SpotifyOAuth
import pywhatkit
import psutil
import sys
import pyjokes
import subprocess


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speake('This is OSCAR an Online System for Companion and Automated Responses')

def show_time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is")
    speak(Time)


def show_date():
    Year = int(datetime.datetime.now().year)
    Month = int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak("The Current date is")
    speak(Date)
    speak(Month)
    speak(Year)

def wish_me():
    speak("Welcome back Master")
   # speak("The current time is")
    show_time()
   # speak("The Current date is")
    show_date()
    Hour = datetime.datetime.now().hour
    if Hour>= 6 and Hour< 12:
        speak('Good Morning Master!')
    elif Hour<=12 and Hour<18:
        speak('Good Afternoon Master!')
    elif Hour>=18 and Hour<24:
        speak('Good Evening Master!')
    else:
        speak('Good Night Master!')
    speak('This is OSCAR an Online System for Companion and Automated Responses , at your service. Please tell me master how can i help you?')




def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')  
        print(query)
      #  return query.lower() 

    except Exception as e:
        print(e)
        speak('say that again please')
        # return None

    return query
# take_command()


def send_email(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('xyz0@gmail.com','18Dec2022')
    server.sendmail('abc@gmail.com',to,content)
    server.close()


def screenshot():
    image = pyautogui.screenshot()
    image.save('E:\OSCAR\Screenshots\ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())


if __name__ =='__main__':
    wish_me()
    while True:
        query = take_command().lower()

        if 'time' in query:
            show_time()
        elif 'date' in query:
            show_date()
        

        elif 'wikipedia' in query:
            speak('Ok Master.Let Me search it for you.')
            wiki_query=query.replace('wikipedia','')
            results=wikipedia.summary(wiki_query,sentences=2)
            print(results)
            speak(results)
        
        elif 'send email' in query:
            try:
                speak('what should I write in Email?')
                content = take_command()
                to = 'abc@gmail.com',
                send_email(to,content)
                speak('Email has been sent successfully.')
            except Exception as e:
                print(e)
                speak('Sorry master,I am unable to send the email..')
        
        elif 'search in chrome' in query:
            speak("what should I search Master.")
            chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"

            query = take_command().lower()
            wb.get(chrome_path).open_new_tab(query+'.com')

        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play' in query:
            speak('Sure , just wait a second .')
            song_name=query.replace('play','')
            print(song_name)
            speak(song_name)
            pywhatkit.playonyt(song_name)
            
        elif 'remember that' in query:
            speak('What should I remember?')
            data = take_command()
            speak('you said me to remember that'+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remembered = open('data.txt','r')
            speak('you said me to remember that'  +remembered.read())

        elif 'screenshot' in query:
            screenshot()
            speak('Done!')

        elif 'CPU' in query:
            cpu()


        elif 'joke' in query:
            jokes()
        
        elif 'whatsapp' in query:
            speak('In which number I should Message?')
            whatsapp_number=take_command()
            phone_number = whatsapp_number.replace(" ", "").replace("-", "")
            number_with_country_code='+91'+whatsapp_number
            speak('what should I message?')
            message_is=take_command()
            
            
            current_time = datetime.datetime.now()
            scheduled_time = current_time + datetime.timedelta(minutes=1)

            time_hour=scheduled_time.hour
            
            time_min=scheduled_time.minute
            pywhatkit.sendwhatmsg(number_with_country_code, message_is, time_hour, time_min)
            speak('sending your message '+message_is+'to the whatsapp number '+phone_number+' with in a minute')
            
            
            
        elif 'offline' in query:
            sys.exit()
            
        