from pipes import quote
import subprocess
import pyautogui as autogui
import sqlite3
import struct
import webbrowser
from engine.configs import Assistant_Name
from playsound import playsound
import eel 
import os
import pywhatkit as kit
import pvporcupine 
import pyaudio
from engine.command import *
from engine.command import speak
from engine.helper import extract_yt_term, remove_words


# connecting to db  
conn = sqlite3.connect("cortex.db")
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


# Creating function for the hotword detection 
def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # using pre trained keywords
        porcupine = pvporcupine.create(access_key='beAmPiXk3oNeekpdhFdAc38//H4hqHBdm61bvxBTLOliOhA1ajwwuQ==',keyword_paths=['E:\\CortexX AI\\cortex_en_windows_v3_0_0.ppn'])
        paud = pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)

        # Loop fpr Streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keywords coming from mic 
            keyword_index = porcupine.process(keyword)

            #checking first keyword detected or not. 
            if keyword_index >= 0 :
                print("Hotword detected")

                #pressing shortcut key i.e Win + C virtually.
                autogui.keyDown("win")
                autogui.press("c")
                time.sleep(2)
                autogui.keyUp("win")

    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()





# Find contacts in db.
def findContact(query):
    
    
    words_to_remove = [Assistant_Name, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
# Whatsapp automation function
def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        cortex_message = "message sent successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        cortex_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        cortex_message = "staring video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    autogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        autogui.hotkey('tab')

    autogui.hotkey('enter')
    speak(cortex_message)