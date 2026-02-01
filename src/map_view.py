import folium
from src.charging_api import get_charging_stations



def create_map(user_lat, user_lon):
    stations = get_charging_stations(user_lat, user_lon)

    ev_map = folium.Map(location=[user_lat, user_lon], zoom_start=12)

    # User marker
    folium.Marker(
        [user_lat, user_lon],
        popup="Your Location",
        icon=folium.Icon(color="blue")
    ).add_to(ev_map)

    # Charging stations
    for station in stations:
        folium.Marker(
            [station["latitude"], station["longitude"]],
            popup=f"{station['name']} | {station['power_kw']} kW",
            icon=folium.Icon(color="green", icon="flash")
        ).add_to(ev_map)

    ev_map.save("ev_map.html")
    print("✅ Map created successfully!")


if __name__ == "__main__":
    create_map(19.0760, 72.8777)
