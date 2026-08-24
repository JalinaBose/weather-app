import tkinter as tk
from tkinter import messagebox
import requests


def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Warning", "Please enter a city name.")
        return

    try:
        # Find city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params
        )

        geo_data = geo_response.json()

        if "results" not in geo_data:
            messagebox.showerror(
                "Error",
                "City not found."
            )
            return

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        city_name = location["name"]
        country = location.get("country", "")

        # Get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params
        )

        weather_data = weather_response.json()

        current = weather_data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        result_label.config(
            text=
            f"📍 {city_name}, {country}\n\n"
            f"🌡️ Temperature: {temperature} °C\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind Speed: {wind_speed} km/h"
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            "Unable to get weather data."
        )


window = tk.Tk()

window.title("Weather App")
window.geometry("500x500")


title = tk.Label(
    window,
    text="Weather App",
    font=("Arial", 24, "bold")
)

title.pack(pady=25)


city_label = tk.Label(
    window,
    text="Enter City Name:",
    font=("Arial", 14)
)

city_label.pack()


city_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=25
)

city_entry.pack(pady=10)


search_button = tk.Button(
    window,
    text="Search Weather",
    font=("Arial", 12),
    command=get_weather
)

search_button.pack(pady=10)


result_label = tk.Label(
    window,
    text="Weather information will appear here.",
    font=("Arial", 13),
    justify="left"
)

result_label.pack(pady=30)


window.mainloop()