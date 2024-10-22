import re
import sqlite3
import webbrowser
from playsound import playsound
from engine.configs import *
from engine.command import *
import eel 
import os
import pywhatkit as kit
from engine.command import speak

# connecting to db  
conn = sqlite3.connect("cortix.db")
cursor = conn.cursor()


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
    
    app_name = query.strip()
    app_name = app_name.capitalize()

    if app_name != "":
        try :
            cursor.execute(
            "SELECT path FROM sys_command WHERE name IN (?)",(app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute("SELECT url FROM web_command WHERE name IN (?)",(app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system("start "+query)
                    except:
                        speak("not found")
        except:
            speak("Soemthing went wrong")



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



