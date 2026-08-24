# Weather App

A Python-based desktop Weather App that allows users to search for a city and view current weather information through a simple graphical user interface.

## Features

- Search weather by city name
- Display current temperature
- Display humidity
- Display wind speed
- Display country and city information
- Real-time weather data from an online API
- User-friendly graphical interface
- Error handling for invalid city names

## Technologies Used

- Python
- Tkinter
- Requests
- Open-Meteo API
- REST API
- Functions
- GUI Programming
- JSON Data

## How to Run

1. Make sure Python is installed on your computer.
2. Install the required Requests library:

```bash
pip install requests
Download or clone this repository.
Open the project folder in VS Code.
Run the following command:
python weather_app.py
How It Works

The application allows users to enter a city name and search for its current weather information.

City Search

The user enters a city name into the search box and clicks the Search Weather button.

Location Data

The application uses the Open-Meteo Geocoding API to find the city's latitude and longitude.

Weather Data

The application then uses the Open-Meteo Weather API to retrieve current weather information.

Weather Information

The application displays:

Temperature in Celsius
Relative humidity
Wind speed
City name
Country
Example
City: Dubai

Temperature: 37.1 °C
Humidity: 45%
Wind Speed: 15 km/h
Project Structure
weather-app/
│
├── weather_app.py
├── README.md
└── .gitignore
API

This project uses the Open-Meteo API to retrieve weather and geolocation data.

No API key is required for this project.

Future Improvements
Add weather condition icons
Add 7-day weather forecast
Add sunrise and sunset information
Add temperature unit selection
Add weather animations
Add more detailed weather information
Improve the graphical interface
Add dark mode

Author
Jaslina Bose
IT Graduate | Python Developer | Web Developer
