from ipaddress import ip_address
import requests
from greet import greet_user
from engine import speak
from user_input import take_user_input
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia
from functions.os_ops import open_calculator, open_camera, open_cmd, open_discord
from pprint import pprint

if __name__ == '__main__':
	greet_user()
	while True:
		query = take_user_input().lower()

		if 'open discord' in query:
			open_discord()

		elif 'open command prompt' in query or 'open cmd' in query:
			open_cmd()

		elif 'open camera' in query:
			open_camera()

		elif 'open calculator' in query:
			open_calculator()

		elif 'ip address' in query:
			ip_address = find_my_ip()
			speak(f"Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.")
			print(f'Your IP Address is {ip_address}')

		elif 'wikipedia' in query:
			speak('What do you want to search on Wikipedia, sir?')
			search_query = take_user_input().lower()
			results = search_on_wikipedia(search_query)
			speak(f"According to wikipedia, {results}")
			speak("For your convenience, I am printing it on the screen sir.")
			print(results)
		
		elif 'youtube' in query:
			speak('What do you want to play on Youtube, sir?')
			video = take_user_input().lower()
			play_on_youtube(video)

		elif 'search on google' in query:
			speak('What do you want to search on Google, sir?')
			query = take_user_input().lower()
			search_on_google(query)
		
		elif 'joke' in query:
			speak(f"Hope you like this one sir")
			joke = get_random_joke()
			speak(joke)
			speak("For your convenience, I am printing it on the screen sir.")
			pprint(joke)
		

		elif "advice" in query:
			speak(f"Here's an advice for you, sir")
			advice = get_random_advice()
			speak(advice)
			speak("For your convenience, I am printing it on the screen sir.")
			pprint(advice)

		elif "trending movies" in query:
			speak(f"Some of the trending movies are: {get_trending_movies()}")
			speak("For your convenience, I am printing it on the screen sir.")
			print(*get_trending_movies(), sep='\n')

		elif 'news' in query:
			speak(f"I'm reading out the latest news headlines, sir")
			speak(get_latest_news())
			speak("For your convenience, I am printing it on the screen sir.")
			print(*get_latest_news(), sep='\n')

		elif 'weather' in query:
			ip_address = find_my_ip()
			city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
			speak(f"Getting weather report for your city {city}")
			weather, temperature, feels_like = get_weather_report(city)
			speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
			speak(f"Also, the weather report talks about {weather}")
			speak("For your convenience, I am printing it on the screen sir.")
			print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")