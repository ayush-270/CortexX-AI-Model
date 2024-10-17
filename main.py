import os
import eel

eel.init("www")

''' Creating app mode for the AI
Initialiasing MS browser to open our index.html file. '''

os.system('start Chrome.exe --app = "http://localhost:8000/index.html"')

eel.start("index.html", block = True)