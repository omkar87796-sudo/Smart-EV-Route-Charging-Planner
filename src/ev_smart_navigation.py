from src.route_navigation import get_route
from src.predict_battery import check_battery
import folium


def smart_ev_navigation():
    start = (72.8777, 19.0760)   # Mumbai
    end = (73.8567, 18.5204)     # Pune

    route, distance = get_route(start, end)
    battery_used = check_battery(distance)

    status = "✅ Battery Sufficient"
    color = "green"

    if battery_used > 45:
        status = "⚠️ Charging Required"
        color = "red"

    print(f"Distance: {distance} km")
    print(f"Battery Used: {battery_used} kWh")
    print(status)

    m = folium.Map(location=[start[1], start[0]], zoom_start=10)
    folium.GeoJson(route).add_to(m)

    folium.Marker(
        [start[1], start[0]],
        popup="Start",
        icon=folium.Icon(color="green")
    ).add_to(m)

    folium.Marker(
        [end[1], end[0]],
        popup=f"{status}\nBattery: {battery_used} kWh",
        icon=folium.Icon(color=color)
    ).add_to(m)

    m.save("route_map.html")
    print("✅ Smart EV route created!")


if __name__ == "__main__":
    smart_ev_navigation()
