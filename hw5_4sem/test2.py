import requests

API_key = "08df79a0cfb21ef760ec9e1ddc9dcea6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("City: ")
url_params = {"appid": API_key, "q": city_name}
weather_data = requests.get(base_url, params=url_params).json()
temperature = weather_data['main']['temp']


print(f"\nTemperature: {temperature}")


