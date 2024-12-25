# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Hi welcome to python'

# Language in which you want to convert
language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welome.mp3")

# Playing the converted file
os.system("start welome.mp3")
