from gtts import gTTS
import  easygui
import os

#enter text window
mytext = easygui.enterbox('Enter your text')

#enter  language tag eg. "en" for english, "fr" for french
language = easygui.enterbox('Enter your language tag ')

myobj = gTTS(text=mytext, lang=language , slow=False)

myobj.save("welcome.mp3")

os.system("welcome.mp3")
