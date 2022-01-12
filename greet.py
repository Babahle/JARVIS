from datetime import date, datetime
from engine import BOTNAME, USERNAME, speak

def greet_user():
	"""Greets the user"""

	hour = datetime.now().hour
	if (hour >= 6) and (hour < 12):
		speak(f"Good morning {USERNAME}")
	elif (hour >= 12) and (hour < 16):
		speak(f"Good afternoon {USERNAME}")
	elif (hour >= 16) and (hour < 19):
		speak(f"Good evening {USERNAME}")
	speak(f"I am {BOTNAME}. How may I assist you")