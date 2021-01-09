import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
print(voices[1].id)
speaker.setProperty('voice',voices[0].id)

def speak(audio):
    speaker.say(audio)
    speaker.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis sir, Please tell me how may I help you!!")    

def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Order...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recoginizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said : {query}\n")

    except Exception:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.ehlo()
    server.login('mavrider007@gmail.com','Mavrick@123')
    server.sendmail('mavrider007@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()
    if 'wikipedia' in query:                            #task 1
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)

    elif 'open command' in query:                       #task 2
        speak("Opening Command Prompt Sir...")
        os.system("start cmd")

    elif 'open youtube' in query:                       #task 3
        speak("Opening YouTube...")
        webbrowser.open('youtube.com')

    elif 'open google' in query:                        #task 4
        speak("Opening Google...")
        webbrowser.open('google.com')

    elif 'open stackoverflow' in query:                 #task 5
        speak("Opening StackOverFlow...")
        webbrowser.open('stackoverflow.com')

    elif 'play music' in query:                         #task 6
        speak("Okay Sir")
        music_dir = 'D:\\opppo\\New folder'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    
    elif 'the time' in query:                           #task 7
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,The time is {strTime}")
    
    elif 'open code' in query:                          #task 8
        path = "C:\\Users\\Mukul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    elif 'send email' in query:                         #task 9
        try:
            speak("What should i say ?")
            content = takeCommand()
            to = "ayushtomar306@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!!")

        except Exception as e:
            print(e)
            speak("Sorry Sir, I unable to Sent...!!!")
    
    # elif 'open webcam' in query:                        #task 10
