import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config("BOTNAME")

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)

engine.setProperty('volume', 190)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
	"""Used to speak whatever text is passed to it"""

	engine.say(text)
	engine.runAndWait()