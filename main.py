import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recognise

def start () :
    eel.init("www")

    ''' Creating app mode for the AI
    Initialiasing MS browser to open our index.html file. '''

    playAssistantSound()
    @eel.expose
    def init():
        # subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for face authentication")
        flag = recognise.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successfull")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome The The CortexX AI Model.")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Failed.")

    #os.system('start Chrome.exe --app = "http://localhost:8000/index.html"')

    eel.start("index.html", block = True) 