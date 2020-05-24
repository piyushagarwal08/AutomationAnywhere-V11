import os
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
output=r.recognize_google(audio)
print("Understood: ",output)
if "launch" in output:
    print("Working.... please wait")
    os.system("Launch_Applications.atmx")
else:
    print("Sorry not Understood")
    
