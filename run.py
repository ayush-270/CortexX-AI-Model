import multiprocessing
import subprocess

# function to make the model run.
def StartCortex():
    # code for process 1
    print("Process 1 is running.")
    from main import start
    start()


#function to run the hotword.
def listenHotWord():
    #code for process 2.
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()


# start both the procsses.
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=StartCortex)
    p2 = multiprocessing.Process(target=listenHotWord)
    p1.start()
    subprocess.call([r'device.bat'])
    p2.start()
    p1.join()
  
    if p2.is_alive():
        p2.terminate()
        p2.join()
 
    print("System stop")



# adb shell am start -a android.intent.action.CALL -d tel:+917988168548
# adb shell input tap 136 2220
# adb shell input text "Ayush%sis%making%sproject"
# adb shell input keyevent 3