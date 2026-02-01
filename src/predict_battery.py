def predict_battery(distance_km, speed, temperature, load):
    base = 0.18
    speed_factor = max(0, (speed - 80) * 0.002)
    temp_factor = abs(25 - temperature) * 0.01
    load_factor = load * 0.002

    return round(distance_km * (base + speed_factor + temp_factor + load_factor), 2)
