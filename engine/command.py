import pyttsx3
import speech_recognition as sr 
import pyaudio as audio
import eel
import time



# Creating the function to make the assistant speak
def speak(text):
    #initiating the voices
    engine = pyttsx3.init("sapi5")

    #getting the voices our system has.
    voices = engine.getProperty('voices')

    #Selecting the voice
    engine.setProperty('voice', voices[0].id)

    #Specifying the auido rate
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    # Initiating it to speak.
    engine.say(text)

    #Displaying the query in chatbox
    eel.receiverText(text)
    engine.runAndWait()

# checking the function.
# speak("Hey there this is you cortex ai")

# Creating the function for speech recognition.
@eel.expose
def TakeCommand():
    # initializing the recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source :
        print("Listening....")
        # Displaying it in app
        eel.DisplayMessage("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source , 10 , 8)


    try:
        print("Recognizing...")
        # Displaying it in app
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")
        # Displaying it in app
        eel.DisplayMessage(query)
        time.sleep(4)
        
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def AllCommands(message=1):
    # Checking if the message is passed or not
    # if it is not passed (i.e message == 1) then taking value from mic. i.e takecommand().
    if message == 1:
        query1 = TakeCommand()
        print(query1)

        #Displaying the query in chatbox
        eel.senderText(query1)
    # if it is passed assigning to the variable query1 for execution.
    else:
        query1 = message

        #Displaying the query in chatbox
        eel.senderText(query1)
    try:

        if "open" in query1:
            from engine.features import OpenCommand
            OpenCommand(query1)

        elif "on youtube" in query1:
            from engine.features import PlayYoutube
            PlayYoutube(query1)

        elif "send message" in query1 or "phone call" in query1 or "video call" in query1:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query1)
            if(contact_no != 0):

                if "send message" in query1:
                    flag = 'message'
                    speak("what message to send")
                    query1 = TakeCommand()
                    
                elif "phone call" in query1:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query1, flag, name)


        else:
            print("not running")

    except:
        print("error")


    eel.DisplayHood()

