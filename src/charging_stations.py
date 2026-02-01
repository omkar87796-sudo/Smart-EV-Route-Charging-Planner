def get_nearby_charging_stations(lat, lon):
    import requests

    API_KEY = "5b74f4c8-5d29-4757-9698-0c61355c0b01"

    url = "https://api.openchargemap.io/v3/poi/"

    params = {
        "key": API_KEY,
        "latitude": lat,
        "longitude": lon,
        "distance": 50,
        "distanceunit": "KM",
        "maxresults": 10
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    return response.json()
