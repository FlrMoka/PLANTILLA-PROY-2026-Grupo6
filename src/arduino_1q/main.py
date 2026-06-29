from flask import Flask, request, jsonify

app = Flask(__name__)

# Últimos valores recibidos desde el ESP32
last_temp = 0.0
last_rpm = 0.0

@app.route("/data", methods=["GET", "POST"])
def data():
    global last_temp, last_rpm

    if request.method == "POST":
        # Llega JSON del ESP32: {"temp": 36.5, "rpm": 40}
        body = request.get_json(force=True, silent=True) or {}
        try:
            last_temp = float(body.get("temp", 0.0))
            last_rpm = float(body.get("rpm", 0.0))
            print(f"Datos recibidos -> Temp: {last_temp:.1f} °C, RPM: {last_rpm:.0f}")
        except Exception as e:
            print("Error parseando JSON:", e)
        return jsonify({"status": "ok"})

    # GET: la página web usa esto para leer los últimos valores
    return jsonify({"temp": last_temp, "rpm": last_rpm})


@app.route("/")
def index():
    # Página sencilla que consulta /data cada 1s
    return """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Monitor RPM y Temperatura</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      background: #111;
      color: #eee;
      text-align: center;
      margin: 0;
      padding: 20px;
    }
    .card {
      margin: 20px auto;
      padding: 20px;
      max-width: 400px;
      background: #222;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    .valor {
      font-size: 2.5rem;
      margin: 10px 0;
    }
    .label {
      font-size: 1rem;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #aaa;
    }
  </style>
</head>
<body>
  <h1>Monitor de Signos</h1>

  <div class="card">
    <div class="label">RPM</div>
    <div id="rpm" class="valor">--</div>
  </div>

  <div class="card">
    <div class="label">Temperatura (°C)</div>
    <div id="temp" class="valor">--</div>
  </div>

  <script>
    async function actualizar() {
      try {
        const res = await fetch('/data');
        if (!res.ok) return;
        const d = await res.json();
        document.getElementById('rpm').textContent =
          (d.rpm !== undefined) ? d.rpm.toFixed(0) : '--';
        document.getElementById('temp').textContent =
          (d.temp !== undefined) ? d.temp.toFixed(1) : '--';
      } catch (e) {
        console.error(e);
      }
    }
    setInterval(actualizar, 1000);
    actualizar();
  </script>
</body>
</html>
    """


if __name__ == "__main__":
    # App Lab ejecuta este script cuando corres la App
    app.run(host="0.0.0.0", port=8080)
