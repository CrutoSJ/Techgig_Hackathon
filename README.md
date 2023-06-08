# Techgig_Hackathon

## Python - Weather Forecasting Tool

This command-line tool accepts a city's name as input and returns the current weather forecast. It utilizes the OpenWeatherMap API to fetch weather data and parses it using Python. The solution demonstrates how GitHub Copilot can assist with API usage, data parsing, and error handling.

## Prerequisites

- Python 3.x
- `requests` library
- `json` library
- `Confidential` module (containing the `API_KEY` variable)
- `prettytable` library
- `colorama` library

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/CrutoSJ/Techgig_Hackathon.git

2. Install the required dependencies:
- pip install -r requirements.txt

3. Set up OpenWeatherMap API Key:

- Obtain an API key from OpenWeatherMap.
- Create a file named Confidential.py in the same directory as the script.
- Add the following line to Confidential.py, replacing YOUR_API_KEY with your actual API key:

   - API_KEY = "YOUR_API_KEY"

## Usage

1. Run the script:

 - python weather_forecast.py

2. Enter the name of the city for which you want to retrieve the weather forecast when prompted.

3. View the current weather forecast displayed in a table format, including temperature, humidity, description, wind speed, and visibility.

- Example Output: 

Enter the city name: New York

- City: New York
- Temperature (°C): 20.53
- Humidity (%): 70
- Description:  Partly cloudy
- Wind Speed (m/s): 5.26
- Visibility (km): 16.09

## License

This project is licensed under the MIT License.


