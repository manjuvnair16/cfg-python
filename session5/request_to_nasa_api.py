import requests

response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
nasa_data = response.json()
print(nasa_data.keys())
print(nasa_data['url'])