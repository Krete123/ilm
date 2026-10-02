import requests

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.437&lon=24.753"

headers = {
    "User-Agent": "krete.kivit@techno.ee"
}

response = requests.get(url, headers=headers)

data = response.json()

timeseries = data["properties"]["timeseries"]

for item in timeseries:
    time = item["time"]
    temperature = item["data"]["instant"]["details"]["air_temperature"]

    print(time, temperature)
