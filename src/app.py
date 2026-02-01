import streamlit as st
import folium
from streamlit_folium import st_folium

from route_navigation import get_route_and_distance
from charging_api import get_nearby_charging_stations
from predict_battery import predict_battery

# ---------------- PAGE CONFIG ----------------
st.set_page_config("EV Smart Navigation", layout="wide")

st.title("🚗 EV Smart Navigation System")

# ---------------- SESSION STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = None

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    start = st.text_input("Start Location", "Mumbai")
    speed = st.slider("Speed (km/h)", 40, 120, 70)
    load = st.slider("Vehicle Load (kg)", 50, 300, 150)

with col2:
    end = st.text_input("Destination", "Goa")
    temp = st.slider("Temperature (°C)", 10, 45, 30)
    battery = st.slider("Battery Capacity (kWh)", 20, 120, 60)

# ---------------- BUTTON ----------------
if st.button("🚀 Plan Route"):
    try:
        route, distance, coords = get_route_and_distance(start, end)

        battery_used = predict_battery(
            distance_km=distance,
            speed=speed,
            temperature=temp,
            load=load
        )

        st.session_state.data = {
            "route": route,
            "distance": distance,
            "coords": coords,
            "battery_used": battery_used
        }

    except Exception as e:
        st.error("❌ Failed to calculate route")
        st.code(str(e))

# ---------------- OUTPUT ----------------
if st.session_state.data:

    data = st.session_state.data

    st.success(f"📏 Distance: {data['distance']:.2f} km")
    st.info(f"🔋 Battery Used: {data['battery_used']:.2f} kWh")

    # Map
    m = folium.Map(
        location=[data["coords"][0][1], data["coords"][0][0]],
        zoom_start=7
    )

    folium.PolyLine(
        [(lat, lon) for lon, lat in data["coords"]],
        color="blue",
        weight=5
    ).add_to(m)

    # Charging station logic
    try:
        mid = data["coords"][len(data["coords"]) // 2]
        stations = get_nearby_charging_stations(mid[1], mid[0])

        for s in stations:
            info = s.get("AddressInfo", {})
            if "Latitude" in info:
                folium.Marker(
                    [info["Latitude"], info["Longitude"]],
                    popup=info.get("Title", "Charging Station"),
                    icon=folium.Icon(color="green", icon="flash")
                ).add_to(m)

    except:
        st.warning("⚠ Could not load charging stations")

    st_folium(m, height=500)