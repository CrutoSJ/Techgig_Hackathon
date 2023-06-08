import requests
import json
import Confidential
from prettytable import PrettyTable
from colorama import Fore, Style

def get_weather(city):
    api_key = Confidential.API_KEY
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
        try:
            main_data = data["main"]
            weather_data = data["weather"][0]
            wind_data = data["wind"]
            visibility = data["visibility"] / 1000  

            temperature = main_data["temp"] - 273.15  
            humidity = main_data["humidity"]
            description = weather_data["description"]
            wind_speed = wind_data["speed"]

            
            table = PrettyTable()
            table.field_names = [Fore.BLUE + "City" + Style.RESET_ALL, Fore.YELLOW + "Temperature (°C)" + Style.RESET_ALL, Fore.GREEN + "Humidity (%)" + Style.RESET_ALL, Fore.CYAN + "Description" + Style.RESET_ALL, Fore.MAGENTA + "Wind Speed (m/s)" + Style.RESET_ALL, Fore.WHITE + "Visibility (km)" + Style.RESET_ALL]
            table.add_row([city, "{:.2f}".format(temperature), humidity, description, wind_speed, "{:.2f}".format(visibility)])  

            
            table.border = True
            table.align = "l"

            
            print(table)
        except KeyError as e:
            print("Failed to retrieve weather data. Error:", e)
            print("API Response:", data)
    else:
        print("City not found.")

city = input("Enter the city name: ")
get_weather(city)
