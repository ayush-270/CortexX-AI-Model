from playsound import playsound
import eel 


# Play Assistant Sound

@eel.expose
def playAssistantSound():
    music_path = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_path)