from gtts import gTTS
import os
class toAudio:
    language='en'
    usertext=input("Enter text: ")
    uservoice=gTTS(text=usertext,lang=language,slow=False)
    uservoice.save('audioout.mp3')
    os.system("audioout.mp3")

nowvoice = toAudio()
nowvoice.usertext
