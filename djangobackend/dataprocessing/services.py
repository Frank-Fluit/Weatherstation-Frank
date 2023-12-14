import requests
import json
import datetime

API_KEY = "4d0a42399d252a0866c7c68630ad09ae"
API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_data_ex_api_loc(city, country_code):
    try:
        api_url = f"{API_BASE_URL}?q={city},{country_code}&APPID={API_KEY}"
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise e


def get_weather_data_by_lat_lon(latitude, longitude):
    try:
        api_url = f"{API_BASE_URL}?lat={latitude}&lon={longitude}&appid={API_KEY}"
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise e


def get_lat_lon_based_loc(city, country_code):
    try:
        response = requests.get(
            "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "," + country_code + "&limit=" + str(
                5) + "&appid=" + API_KEY)
        response.raise_for_status()
        data = response.json()
        first_location = data[0]
        latitude = first_location["lat"]
        longitude = first_location["lon"]
        return latitude, longitude
    except requests.RequestException as e:
        raise e



def get_ex_api_lat_lon_pred(latitude, longitude):
    try:

        response = requests.get("http://api.openweathermap.org/data/2.5/forecast?lat="+str(latitude)+"&lon="+str(longitude)+"&appid="+API_KEY)

        time_records = []
        response = response.json()

        for record in response['list']:
            timestamp_str = record['dt_txt']
            timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            temperature = record['main']['temp'] -272.15

            time_record = {'time': timestamp.isoformat() + 'Z', 'value': temperature}
            time_records.append(time_record)

        for record in time_records:
            print(record)

        return time_records
    except requests.RequestException as e:
        raise e