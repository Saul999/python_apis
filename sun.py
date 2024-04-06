import requests

LAT = 34.052235
LONG = -118.243683
parameters = {
    "lat": LAT,
    "long": LONG
}
response = requests.get("https://api.sunrisesunset.io/json?lat=34.19801&lng=-118.26102", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]['sunrise']
sunset = data["results"]['sunset']

print(sunrise)
print(data)
