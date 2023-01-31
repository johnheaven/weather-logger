import requests
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from os import environ as os_environ

key_file = os_environ['GCP_KEY_FILENAME']
open_weather_key = os_environ['OPEN_WEATHER_KEY']
project_id = os_environ['GCP_PROJ_ID']
table_name = os_environ['TABLE_NAME']
lat = os_environ['LATITUDE']
lon = os_environ['LONGITUDE']

credentials = service_account.Credentials.from_service_account_file(key_file)


# get the data from the API
params = {
    'lat': lat,
    'lon': lon,
    'appid': open_weather_key,
    'units': 'metric',
    'lang': 'en'
}

r = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather', params=params)

# put it into a Pandas DataFrame

data = r.json()

cols = {
    'main': data['weather'][0]['main'],
    'description': data['weather'][0]['description'],
    'temp': data['main']['temp'],
    'feels_like': data['main']['feels_like'],
    'temp_min': data['main']['temp_min'],
    'temp_max': data['main']['temp_max'],
    'pressure': data['main']['pressure'],
    'humidity': data['main']['humidity'],
    'visibility': data['visibility'],
    'wind_speed': data['wind']['speed'],
    'wind_deg': data['wind']['deg'],
    'sunrise': data['sys']['sunrise'],
    'sunset': data['sys']['sunset'],
    'sys_id': data['sys']['id'],
    'timestamp': data['dt'],
    'latitude': lat,
    'longitude': lon
},

df = pd.DataFrame(cols)

# put it somewhere in the Cloud
df.to_gbq(
    destination_table=table_name,
    project_id=project_id,
    credentials=credentials,
    if_exists='append')