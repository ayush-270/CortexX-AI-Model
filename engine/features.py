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
from hugchat import hugchat


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
        target_tab = 6
        message = ''
        cortex_message = "calling to "+name

    else:
        target_tab = 5
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


# Creating function for chatbot

<<<<<<< HEAD
=======
# def chatBot(query):
#     user_input = query.lower()
#     chatbot = hugchat.ChatBot(cookie_path = "engine\\cookies.json")
#     id = chatbot.new_conversation()
#     chatbot.change_conversation(id)
#     response = chatbot.chat(user_input)
#     print(response)
#     speak(response)
#     return response



# Setting up API key

load_dotenv("engine/api.env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

>>>>>>> 945486e (`Update .gitignore to ignore engine/api.env and add it to the list of ignored files. Update load_dotenv() in engine/features.py to load from engine/api.env instead of the default location.`)
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path = "engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response

# Android Automation
# function to make a phone call
def makeCall(name, mobileNo):
    mobileNo = mobileNo.replace(" "," ")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)

# function to send message
def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(320, 2220)
    #start chat
    tapEvents(800, 2195)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(601, 574)
    # tap on input
    tapEvents(390, 2270)
    #message
    adbInput(message)
    #send
    tapEvents(957, 1630)# 1397
    speak("message sent successfully to "+name)



# adb shell am start -a android.intent.action.CALL -d tel:+91
# adb shell input tap 136 2220
# adb shell input text "Ayush%sis%making%sproject"
# adb shell input keyevent 3
