import pyttsx3


# Creating the function to make the assistant speak

def speak(text):
    #initiating the voices
    engine = pyttsx3.init("sapi5")

    #getting the voices our system has.
    voices = engine.getProperty('voices')
    print(voices)

    #Selecting the voice
    engine.setProperty('voice', voices[0].id)

    #Specifying the auido rate
    engine.setProperty('rate', 174)

    # Initiating it to speak.
    engine.say(text)
    engine.runAndWait()

# checking the function.
speak("Hey there this is you cortix ai")