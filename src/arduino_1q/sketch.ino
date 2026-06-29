#include <Arduino_RouterBridge.h>
#include <Wire.h>
#include <U8g2lib.h>

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, U8X8_PIN_NONE);

float temperatura = 0;
float rpm = 0;
bool alarma = false;
String estadoTemp = "SIN DATOS";
String estadoResp = "SIN DATOS";

const unsigned long TIMEOUT = 5000;
unsigned long ultimoPaquete = 0;
int rpmMinNormal = 30;
int rpmMaxNormal = 60;

void evaluarEstados() {
  alarma = false;
  if (temperatura<=33.9)       { estadoTemp="HIPOT.SEV";  alarma=true; }
  else if (temperatura<=35.5)  { estadoTemp="HIPOTERMIA"; alarma=true; }
  else if (temperatura<=37.9)  { estadoTemp="NORMAL"; }
  else if (temperatura<=40.0)  { estadoTemp="FIEBRE";     alarma=true; }
  else                         { estadoTemp="HIPERTERM";  alarma=true; }

  if (rpm<rpmMinNormal)        { estadoResp="APNEA";      alarma=true; }
  else if (rpm>rpmMaxNormal)   { estadoResp="TAQUIPNEA";  alarma=true; }
  else                         { estadoResp="NORMAL"; }
}

void actualizarDatos(float temp, float r) {
  temperatura=temp; rpm=r; ultimoPaquete=millis(); evaluarEstados();
}

void setup() {
  Serial.begin(115200);
  Bridge.begin();
  Bridge.provide("actualizar_datos", actualizarDatos);
}

void loop() {
  delay(100);
}#include <Arduino_RouterBridge.h>
#include <Wire.h>
#include <U8g2lib.h>

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, U8X8_PIN_NONE);

float temperatura = 0;
float rpm = 0;
bool alarma = false;
String estadoTemp = "SIN DATOS";
String estadoResp = "SIN DATOS";

const unsigned long TIMEOUT = 5000;
unsigned long ultimoPaquete = 0;
int rpmMinNormal = 30;
int rpmMaxNormal = 60;

void evaluarEstados() {
  alarma = false;
  if (temperatura<=33.9)       { estadoTemp="HIPOT.SEV";  alarma=true; }
  else if (temperatura<=35.5)  { estadoTemp="HIPOTERMIA"; alarma=true; }
  else if (temperatura<=37.9)  { estadoTemp="NORMAL"; }
  else if (temperatura<=40.0)  { estadoTemp="FIEBRE";     alarma=true; }
  else                         { estadoTemp="HIPERTERM";  alarma=true; }

  if (rpm<rpmMinNormal)        { estadoResp="APNEA";      alarma=true; }
  else if (rpm>rpmMaxNormal)   { estadoResp="TAQUIPNEA";  alarma=true; }
  else                         { estadoResp="NORMAL"; }
}

void actualizarDatos(float temp, float r) {
  temperatura=temp; rpm=r; ultimoPaquete=millis(); evaluarEstados();
}

void setup() {
  Serial.begin(115200);
  Bridge.begin();
  Bridge.provide("actualizar_datos", actualizarDatos);
}

void loop() {
  delay(100);
}
