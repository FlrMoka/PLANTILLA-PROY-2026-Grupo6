#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <MPU9250_asukiaaa.h>

const char* ssid = "A17";
const char* password = "00001111";

// Envío directo a Replit
const char* serverName = "https://esp-web-host--miguelllancao20.replit.app/api/sensor/data";

#define TEMP_PIN 34

MPU9250_asukiaaa mpu;

// --- VARIABLES PARA EL PROMEDIO MÓVIL DE RPM ---
const int NUM_LECTURAS = 3;
float lecturasRPM[NUM_LECTURAS];
int indiceLectura = 0;
float sumaRPMTotal = 0;
float rpmPromedioFinal = 0;

// --- CONTROL DE RESPIRACIÓN (EJE Y) ---
float yPromedio = 0;
unsigned long lastRespTime = 0;
bool arriba = false;
unsigned long ultimaTransmision = 0;

// --- CONTROL DE REPOSO / DETECCIÓN DE 0 RPM ---
unsigned long ultimoMovimientoValidoTime = 0;

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);

  mpu.setWire(&Wire);
  mpu.beginAccel();

  if (mpu.accelUpdate() != 0) {
    Serial.println("No se detectó el MPU9250");
    while (1);
  }

  mpu.accelUpdate();
  yPromedio = mpu.accelY();
  lastRespTime = millis();
  ultimoMovimientoValidoTime = millis();
  ultimaTransmision = millis();

  for (int i = 0; i < NUM_LECTURAS; i++) {
    lecturasRPM[i] = 0;
  }
  sumaRPMTotal = 0;
  rpmPromedioFinal = 0;

  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado. IP: " + WiFi.localIP().toString());
}

void loop() {
  if (mpu.accelUpdate() != 0) {
    delay(10);
    return;
  }

  unsigned long currentTime = millis();
  float currentY = mpu.accelY();

  // Filtro pasa-bajas (RPM)
  yPromedio = 0.93 * yPromedio + 0.07 * currentY;
  float diffY_resp = currentY - yPromedio;

  if (abs(diffY_resp) > 0.008) {
    ultimoMovimientoValidoTime = currentTime;
  }

  // --- DETECTOR DE RESPIRACIÓN ---
  if (!arriba && diffY_resp > 0.02) {
    arriba = true;
    unsigned long timeGap = currentTime - lastRespTime;
    if (timeGap >= 1200 && timeGap <= 8000) {
      float rpmInstantnea = 60000.0 / timeGap;
      sumaRPMTotal = sumaRPMTotal - lecturasRPM[indiceLectura];
      lecturasRPM[indiceLectura] = rpmInstantnea;
      sumaRPMTotal = sumaRPMTotal + lecturasRPM[indiceLectura];
      indiceLectura = (indiceLectura + 1) % NUM_LECTURAS;
      rpmPromedioFinal = sumaRPMTotal / NUM_LECTURAS;
      Serial.printf("\n---> [RESPIRACIÓN] Ciclo: %.2fs | RPM Inst: %.1f | Promedio: %.1f\n\n",
                    timeGap / 1000.0, rpmInstantnea, rpmPromedioFinal);
      lastRespTime = currentTime;
    } else if (timeGap > 8000) {
      lastRespTime = currentTime;
    }
  }

  if (diffY_resp < -0.02) {
    arriba = false;
  }

  // --- AUTO-CERO: 7s de inactividad → RPM = 0 ---
  if (currentTime - ultimoMovimientoValidoTime > 7000) {
    rpmPromedioFinal = 0;
    sumaRPMTotal = 0;
    for (int i = 0; i < NUM_LECTURAS; i++) lecturasRPM[i] = 0;
  }

  // --- ENVÍO HTTP CADA 1 SEGUNDO ---
  if (currentTime - ultimaTransmision >= 1000) {
    int lectura = analogRead(TEMP_PIN);
    
    // 1. Calculamos el voltaje en el pin (máximo 3.3V / 3300mV)
    float voltajePin = lectura * (3300.0 / 4095.0);
    
    // 2. Reconstruimos el voltaje original del LM35 (escala 5V) tras el divisor
    float voltajeRealLM35 = voltajePin * 1.666; 
    
    // ====================================================================
    // AJUSTE DE PRECISIÓN EN AMBIENTE (OFFSET):
    // Si la lectura marca muy abajo de lo real debido a la baja sensibilidad,
    // puedes sumar o restar un valor de desfase aquí.
    // ====================================================================
    float offsetTemperatura = 4.5; // Suma 4.5 grados para compensar la pérdida del ADC
    
    // 3. Fórmula del LM35 + Compensación
    float temperatura = (voltajeRealLM35 / 10.0) + offsetTemperatura;

    Serial.printf("Volt_Pin: %.1f mV | Temp LM35: %.1f C | RPM: %.0f\n",
                  voltajePin, temperatura, rpmPromedioFinal);

    if (WiFi.status() == WL_CONNECTED) {
      WiFiClient client;
      HTTPClient http;

      http.setTimeout(5000);
      http.begin(serverName);
      http.addHeader("Content-Type", "application/json");

      String body = "{\"temperature\":" + String(temperatura, 1) +
                    ",\"breathing_rate\":" + String(rpmPromedioFinal, 0) +
                    ",\"device_id\":\"esp32-baby\"}";

      int codigo = http.POST(body);

      if (codigo > 0) {
        Serial.println("Replit OK: " + String(codigo));
      } else {
        Serial.println("Error: " + http.errorToString(codigo));
        WiFi.reconnect();
      }

      http.end();
    } else {
      Serial.println("WiFi perdido, reconectando...");
      WiFi.reconnect();
    }

    ultimaTransmision = millis();
  }

  delay(20);
}
