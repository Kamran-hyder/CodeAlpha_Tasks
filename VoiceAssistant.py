# Import some modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)

# Setting David Voice
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# Functions
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir, Lemme know How may I help you?")

def takeCommand():
    # It takes mic input from the user and returns string output of microphone.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        # r.pause_sound()
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        # speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

# Main Method
if __name__ == '__main__':
    # speak("My name is Kamran Hyder")
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'Wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")
            # speak("According to YouTube")
            # webbrowser.open(query)

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening Stack Overflow")

        elif 'open github' in query:
            webbrowser.open("github.com")
            speak("Opening Github")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            speak("Opening LinkedIn")

        elif 'play songs of arijit singh' or 'arijit singh ke gaane' in query:
            music_dir = "C:\\Users\\Hp\\Desktop\\Internship_Tasks\\Assets\\Songs\\Arijit Singh Songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
            speak("Playing Music")

        elif 'play songs of sonu nigam' or 'sonu nigam ke gaane' in query:
            music_dir = "C:\\Users\\Hp\\Desktop\\Internship_Tasks\\Assets\\Songs\\Sonu Nigam Songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing Music")

        elif 'open vs code' or 'vs code' in query:
            vscodepath = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)
            print(vscodepath)
            speak("Opening VS Code")

        elif 'What time is it' or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        else:
            speak("Say that again please...")