import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import wolframalpha
import pyjokes
import smtplib
import time
from selenium import webdriver
from ecapture import ecapture as ec
from urllib.parse import quote

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greet():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("Welcome , I am your personal voice assistant")

def VoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        work = r.recognize_google(audio, language='en-in')
        print(f"User said: {work}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice.")
        return "None"
    return work

def countdown(n) :
    while n > 0:
        print (n)
        n = n - 1
    if n ==0:
        print('BLAST OFF!')

def usrname():
    speak("What should i call you sir")
    uname=takeCommandname()
    speak("Welcome Mister")
    speak(uname)
    print("#####################")
    print("Welcome Mr.",uname)
    print("#####################")

def takeCommandname():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Username...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Trying to Recognizing Name...")
        work = r.recognize_google(audio, language='en-in')
        print(f"User said: {work}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognizing your name.")
        takeCommandname()
        return "None"
    return work

def takeCommandmessage():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Enter Your Message")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        work = r.recognize_google(audio, language='en-in')
        print(f'Message to be sent is : {work}\n')

    except Exception as e:
        print (e)
        print("Unable to recognize your message")
        print("Check your Internet Connectivity")
    return work

def takeCommanduser():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Name of User or Group")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        work = r.recognize_google(audio, language='en-in')
        print(f'Client to whome message is to be sent is : {work}\n')

    except Exception as e:
        print (e)
        print("Unable to recognize Client name")
        speak("Unable to recognize Client Name")
        print("Check your Internet Connectivity")
    return work

def takeCommandcontent():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What Should i say, sir")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        work = r.recognize_google(audio, language='en-in')
        print(f'Message to be sent is: {work}\n')

    except Exception as e:
        print (e)
        print("Unable to recognize")
    return work

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('varikallumanojkumar15@gmail.com', 'manoj@1512')
    server.sendmail('varikallumanojkumar15@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    while True:
        work = VoiceCommand().lower()
        if 'hello' in work or 'friday' in work:
            greet()
            usrname()
            speak('how can i help you')
        
        if "wikipedia" in work:
            speak("Searching wikipedia...")
            work = work.replace("wikipedia", "")
            results = wikipedia.summary(work,sentences =5)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in work:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open google' in work:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.co.in/")

        elif 'open mail' in work:
            speak("Here you go to mail\n")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open whatsapp' in work:
            speak("opening whatsApp for you\n")
            webbrowser.open("https://web.whatsapp.com/")
        
        elif "send a whatsapp message" in work or "send a whatsaap message" in work:
            driver = webdriver.Chrome('Web Driver Location')
            driver.get('https://web.whatsapp.com/')
            speak("Scan QR code before proceding")
            tim=10
            time.sleep(tim)
            speak("Enter Name of Group or User")
            name = takeCommanduser()
            speak("Enter Your Message")
            msg = takeCommandmessage()
            count = 1
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()
            msg_box = driver.find_element_by_class_name('_3u328')
            for i in range(count):
                msg_box.send_keys(msg)
                button = driver.find_element_by_class_name('_3M-N-')
                button.click()

        elif 'the time' in work:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to jaggu' in work:
            try:
                content = takeCommandcontent()
                to = "jagadeshwarjaggu2003@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        
        elif "who made you" in work or "who created you" in work:
            speak("I have been created by Manoj.")

        elif 'joke' in work:
            speak(pyjokes.get_joke())

        elif "calculate" in work:
            app_id = "Wolframe Alpha API"
            client = wolframalpha.Client(app_id)
            indx = work.lower().split().index('calculate')
            work = work.split()[indx + 1:]
            res = client.work(' '.join(work))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        
        elif 'search' in work or 'play' in work:
            work = work.replace("search", "")
            work = work.replace(" ", "")
            #search_query = quote(work)
            print(work)
            search_url = f"https://www.google.com/search?q={work}"
            webbrowser.open(search_url)
            #webbrowser.open(work)
        
        elif "camera" in work or "take a photo" in work:
            ec.capture(0,"Jarvis Camera ","img.jpg")

        elif "countdown of" in work:
            work = int(work.replace("countdown of ",""))
            countdown(work)

        elif "write a note" in work:
            speak("What should i write , sir")
            note= VoiceCommand()
            file = open('friday3.txt','w')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
            file.close()
        
        elif 'exit' in work:
            speak("Call me if you need any assistance ..... Thankyou and have a nice day....")
            exit()
        