"""
Baby Monitor - Arduino 1Q Python Server
========================================
Corre en la parte Linux del Arduino 1Q.

Flujo:
  ESP32  -->  POST http://<IP-ARDUINO>:8080/data  -->  este servidor
  Este servidor  -->  POST https://TU-APP/api/sensor/data  -->  Dashboard web

Instalar dependencias:
  pip install flask requests

Correr:
  python3 arduino_server.py
"""

from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# =====================================================
# CONFIGURA ESTO antes de correr
# =====================================================
# URL del dashboard publicado en Replit.
# Después de publicar la app, reemplaza con tu URL real.
DASHBOARD_API_URL = "https://TU-APP.replit.app/api/sensor/data"

# Puerto donde este servidor escucha al ESP32.
# Debe coincidir con serverName en el código del ESP32.
LISTEN_PORT = 8080
# =====================================================

last_reading = None


def forward_to_dashboard(temp: float, rpm: float, device_id: str = "esp32-baby"):
    """Reenvía los datos recibidos del ESP32 al dashboard web."""
    payload = {
        "temperature": temp,
        "breathing_rate": rpm,
        "device_id": device_id,
    }
    try:
        resp = requests.post(DASHBOARD_API_URL, json=payload, timeout=5)
        if resp.status_code == 201:
            print(f"  Dashboard OK")
        else:
            print(f"  Dashboard error: {resp.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"  Sin conexion al dashboard (verifica la URL o el internet)")
    except requests.exceptions.Timeout:
        print(f"  Dashboard timeout")
    except Exception as e:
        print(f"  Error: {e}")


@app.route("/data", methods=["POST"])
def receive_from_esp32():
    """
    El ESP32 hace POST a http://<IP-ARDUINO-1Q>:8080/data
    con JSON: {"temp": 36.7, "rpm": 42}
    """
    global last_reading

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "No se recibio JSON valido"}), 400

    temp = data.get("temp")
    rpm  = data.get("rpm")

    if temp is None or rpm is None:
        return jsonify({"error": "Faltan campos: se requieren 'temp' y 'rpm'"}), 400

    temp = float(temp)
    rpm  = float(rpm)

    last_reading = {"temp": temp, "rpm": rpm, "received_at": datetime.now().isoformat()}

    print(f"[{datetime.now().strftime('%H:%M:%S')}] ESP32: Temp={temp:.1f}C  RPM={rpm:.0f}")

    forward_to_dashboard(temp, rpm)

    return jsonify({"status": "ok", "temp": temp, "rpm": rpm}), 200


@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "running",
        "listen_port": LISTEN_PORT,
        "dashboard_url": DASHBOARD_API_URL,
        "last_reading": last_reading,
    })


if __name__ == "__main__":
    print("=" * 50)
    print("Baby Monitor - Arduino 1Q Server")
    print(f"Puerto: {LISTEN_PORT}")
    print(f"Dashboard: {DASHBOARD_API_URL}")
    print("=" * 50)
    app.run(host="0.0.0.0", port=LISTEN_PORT, debug=False)
