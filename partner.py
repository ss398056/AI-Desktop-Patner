import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#print(voices[2])


def speak(audio):
    print("Speak :",audio)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
            
    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
     
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am AI Desktop Partner, How may I help you?")
        
def sendEmail(to, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sandeepproject76@gmail.com','faygskguerpcxoit')
    server.sendmail('sandeepproject76@gmail.com', to, body)
    server.close()
            
    
if __name__ == "__main__":
    wishMe()
    #speak("This is AI Partner")
    while True :
        query = takeCommand().lower()
        
        if 'wikipedia' in query :
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            speak(result)
        elif 'open youtube' in query :
            webbrowser.open("youtube.com")
        #elif 'open google' in query :
        #    webbrowser.open("google.com")
        elif 'play music' in query :
            music_dic = "E:\\music"
            songs = os.listdir(music_dic)
            print(songs)
            songs_len = len(songs)
            song_no = random.randint(0,songs_len)            
            os.startfile(os.path.join(music_dic, songs[song_no]))        
        elif 'time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strTime}")
        elif 'date' in query :
            strDate = datetime.datetime.now().strftime("%d %b %Y")
            speak(f"Today is {strDate}")
        elif 'open vs code' in query :
            path = "C:\Program Files\Microsoft VS Code\Code.exe"
            os.startfile(path)
        elif 'open google chrome' in query :
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif 'send email' in query :
            try :
                speak("What shoud I say?")
                content = takeCommand()
                to = "ss398056@gmail.com"
                sendEmail(to,content)
                speak("Email has been suscessfully sent!")
            except Exception as e :
                print(e)
                speak("Something went wrong! Email has been not sent, try again.")
        elif 'exit' in query :
            break
    