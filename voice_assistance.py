# say hello to start Devid
# say bye to exit
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    '''its wish the user as per the time'''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("good morning boss have a good day!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon boss!")
    elif hour >= 18 and hour < 24:
        speak("good evening boss!")

    speak("i am Devid. please tell me how may i help you")


def command():
    '''it takes microphone input and gives string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        print("say it again please......\n")
        return "None"
    return query


if __name__ == "__main__":
    print("""you can give command to devid using these:
                                        wikipedia\n
                                        youtub\n
                                        HackerRank\n
                                        music\n
                                        time\n
                                        shopping\n
                                        """)
    while True:
        query = command().lower()

        if 'wikipedia' in query:
            speak("searching.....")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'youtub' in query:
            speak("opening youtub....")
            chrom_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrom_path).open("https://www.youtube.com/")

        elif 'music' in query:
            music_dir = 'D:\\my songs\\my songs'
            songs = os.listdir(music_dir)
            random.shuffle(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir the time is {time}")

        elif 'open code' in query:
            code_path = 'C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(code_path)
            speak("happy coding boss!")

        elif 'hackerrank' in query:
            speak('opening hackerrank...')
            chrom_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrom_path).open(
                "https://www.hackerrank.com/dashboard")

        elif 'shopping' in query:
            speak('here is your result...')
            chrom_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrom_path).open("https://www.flipkart.com/")

        elif 'hello' in query:
            wish_me()

        elif 'by' in query:
            speak("see you soon boss")
            exit()
