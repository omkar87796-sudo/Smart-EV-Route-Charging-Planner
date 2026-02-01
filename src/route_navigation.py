import openrouteservice

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImMwNDIzYjRjOTcxZjQ5ZmI5ZTI3Y2Y0NGU4NTg2YWI5IiwiaCI6Im11cm11cjY0In0="

client = openrouteservice.Client(key=API_KEY)


def get_coordinates(place):
    response = client.pelias_search(text=place)

    if not response["features"]:
        raise Exception(f"Location not found: {place}")

    coords = response["features"][0]["geometry"]["coordinates"]
    return coords  # [lon, lat]


def get_route_and_distance(start, end):
    start_coords = get_coordinates(start)
    end_coords = get_coordinates(end)

    route = client.directions(
        coordinates=[start_coords, end_coords],
        profile="driving-car",
        format="geojson"
    )

    distance_km = (
        route["features"][0]["properties"]["summary"]["distance"] / 1000
    )

    coords = route["features"][0]["geometry"]["coordinates"]

    return route, distance_km, coords
