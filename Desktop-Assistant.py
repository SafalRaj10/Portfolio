import os
from win10toast import ToastNotifier
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pyautogui
from tkinter import filedialog
import random
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 165)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(speak):
    engine.say(speak)
    engine.runAndWait()
# speak("Engine Started")
# speak("Good Morning")
toast=ToastNotifier()
toast.show_toast("Voice Assistant","Voice Assist has started", duration=3)    #For notification in windows
def takescreenshot1():
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename()
    myScreenshot.save(file_path)
while True:
    input = sr.Recognizer()                           #initiating voice recognizer
    input.dynamic_energy_threshold=False              #auto sound energy detection is off so we can manually adjust energy threshold
    input.energy_threshold = 800                      #noise filtering. Keep it higher if microphone is sensitive
    with sr.Microphone() as source:                   #choosing default microphone as our source microphone

        try:
            print("listening")
            input.non_speaking_duration = 0.4         #seconds of non-speaking audio to keep on both sides of the recording
            input.pause_threshold = 0.4               #seconds of non-speaking audio before a phrase is considered complete
            audio = input.listen(source)              #listening audio
            print("recognizing")
            data = input.recognize_google(audio)      #using google engine to recognize audio
            data = data.lower()
            print(data)


        except Exception as e:
            print("Could not hear that")
            data="null data"
            continue
        '''
        Now that you have the voice as a data, you can use it as a command to operate your PC.
        '''
        if (""):
            pass
        elif ("open microsoft edge" in data or "open edge" in data or "open age" in data or "edge open" in data or "age open" in data or "h open" in data):
            print("opening Edge")
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        elif ("open chrome" in data or "open google chrome" in data or "chrome open" in data or "google chrome" in data or "chrome kholo" in data or "google chrome kholo" in data):
            print("opening Chrome")
            os.startfile('C:\Program Files\Google\Chrome\Application/chrome.exe')   #location of your file
        elif("open command prompt" in data or 'open cmd' in data or "open command" in data):
            print("opening Command Prompt")
            os.startfile("C:/Users/91785/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk")
        elif ("open code" in data or "open good" in data or "open cold" in data or "open vs code" in data or "open vidual studio code" in data or "open visual studio" in data or "open court" in data):
            print("opening Visual Studio Code")
            os.startfile("C:/Users/91785/AppData/Local/Programs/Microsoft VS Code/Code.exe")    #location of your file
        elif ("open pycharm" in data or "start pycharm" in data):
            os.system('pycharm')
            ''' this methode returns same as what CMD returns.
             For this to work you must have to have pycharm added to path '''
        elif ("open android studio" in data):
            os.startfile("C:\Program Files\Android\Android Studio/bin\studio64")
            print("Opening Android Studio")
        elif ("open control panel" in data):
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Immersive Control Panel.lnk")
        elif ("open youtube" in data):
            webbrowser.open("https://youtube.com/")
        elif ("take screenshot" in data or "take a screenshot" in data or "screenshot take" in data or "take screenshots" in data):
            try: takescreenshot1()
            except Exception: pass
        elif ("what is" in data or "what's" in data or "what do" in data or "what does" in data or "what can" in data or "how" in data):
            webbrowser.open("https://google.com/search?q="+data)
        elif ("search " in data or "what is" in data):
            data = data.replace("search google", "")
            data = data.replace("search", "")
            webbrowser.open("https://google.com/search?q="+data)
        elif ("wikipedia" in data or "read wikipedia" in data):
            try:
                data = data.replace("read wikipedia ", "")
                data = data.replace(" read wikipedia", "")
                data = data.replace("search wikipedia ", "")
                data = data.replace(" search wikipedia", "")
                data = data.replace(" open wikipedia", "")
                data = data.replace("open wikipedia ", "")
                data = data.replace("wikipedia ", "")
                data = data.replace(" wikipedia", "")
                wikipedia.set_lang("en")
                wp = wikipedia.page(title=data)
                summary = wikipedia.summary(data, sentences=2)
                print(summary)
                webbrowser.open(wp.url)
                # speak(summary)                            #speak function to speak the text retrieved from wikipedia
            except Exception:
                speak("Sorry, Could not process that")
        elif ("play song" in data or "play songs" in data or "play a song" in data or "play music" in data):
            path = random.choice(os.listdir("C:/Users/91785/Music"))            #path to your music flder
            os.startfile(os.path.join("C:/Users/91785/Music", path))
            print("playing", path)
        elif ("confirm shutdown" in data or"shutdown confirm" in data): os.system("shutdown /s /t 5")
        elif ("confirm restart" in data or"restart confirm" in data): os.system("shutdown /r /t 5")
