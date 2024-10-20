import os
import eel

from engine.features import *
from engine.command import *

eel.init("www")

''' Creating app mode for the AI
Initialiasing MS browser to open our index.html file. '''


playAssistantSound()

os.system('start Chrome.exe --app = "http://localhost:8000/index.html"')

eel.start("index.html", block = True)