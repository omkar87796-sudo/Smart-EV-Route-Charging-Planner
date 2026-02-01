import requests

API_KEY = "5b74f4c8-5d29-4757-9698-0c61355c0b01"

def get_nearby_charging_stations(lat, lon, radius=80):
    url = "https://api.openchargemap.io/v3/poi/"
    
    params = {
        "key": API_KEY,
        "latitude": lat,
        "longitude": lon,
        "distance": radius,
        "distanceunit": "KM",
        "maxresults": 10
    }

    headers = {
        "User-Agent": "EV-App"
    }

    r = requests.get(url, params=params, headers=headers)

    if r.status_code == 200:
        return r.json()
    return []
