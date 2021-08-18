from datetime import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  

def wishme():
    hour = int(datetime.now().hour)
    
    if hour > 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good evening Sir")
    speak("I am jarvis, how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
             print("Recognizing...")    
             query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
             print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
        # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishme()
    while True:
        
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            ws=query.replace("wikipedia","")
            result=wikipedia.summary(ws,sentences=4)
            speak("According to wikipedia")
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "the time" in query:
            time=datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")
        elif "open code" in query:
            os.startfile(r"C:\Users\PRANAV ARYA\AppData\Local\Programs\Microsoft VS Code\Code.exe")
        elif "open figma" in query:
            os.startfile(r"C:\Users\PRANAV ARYA\AppData\Local\Figma\Figma.exe")
        elif "open 1 note" in query:
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE")
        elif "quit" in query:
            break
speak("Thank you , hope you have a nice day ahead")