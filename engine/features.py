import re
from playsound import playsound
from engine.configs import *
from engine.command import *
import eel 
import os
import pywhatkit as kit


# Play Assistant Sound

@eel.expose
def playAssistantSound():
    music_path = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_path)

@eel.expose
def OpenCommand(query):
    query = query.replace(Assistant_Name,"")
    query = query.replace("open","")
    query.lower()
    
    if query != "":
        speak("Opening "+query)
        os.system("start "+query)

    else:
        speak("Not Found")


# Function to play on yt.
@eel.expose
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing "+search_term+" on youtube")
    kit.playonyt(search_term)


# Function to get the query for youtube.
@eel.expose
def extract_yt_term(command):
    #defining a expression to get the yt command
    pattern = r"play\s+(.*?)\s+on\s+youtube"
    # using re.search to find the command in the query
    match = re.search( pattern , command , re.IGNORECASE )
    # if found the match return the extracted song/video
    return match.group(1) if match else None