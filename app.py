import requests

from flask import Flask, render_template, request

app = Flask(__name__)

ciudades = {
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Córdoba": {"lat": -31.4201, "lon": -64.1888},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Nueva York": {"lat": 40.7128, "lon": -74.0060},
    "Tokio": {"lat": 35.6895, "lon": 139.6917},
    "París": {"lat": 48.8566, "lon": 2.3522},
    "Londres": {"lat": 51.5074, "lon": -0.1278},
    "Sídney": {"lat": -33.8688, "lon": 151.2093},
    "Ciudad de México": {"lat": 19.4326, "lon": -99.1332},
    "El Cairo": {"lat": 30.0444, "lon": 31.2357}
}

@app.route('/')
def index():
    return render_template(
        'index.html',
        ciudades = ciudades
    )

@app.route('/clima')
def clima():
    ciudad = request.args.get("ciudad")
    coords = ciudades.get(ciudad)

    if not coords:
        return f"No se encontró la ciudad: {ciudad}", 404

    print(f"Ciudad: {ciudad}")
    print(f"Coordenadas: {coords}")

    lat = coords["lat"]
    lon = coords["lon"]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        return "Error al consultar el clima", 500

    datos = respuesta.json()
    clima_actual = datos.get("current_weather", {})

    return render_template('clima.html', ciudad=ciudad, clima=clima_actual)
    



