# PROY-2026-GRUPO6

Repositorio del grupo 6 para el proyecto del ramo *Proyecto Inicial (IWG400)* – 2026.

## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol USM      |
| ----------------- | -------------- | ------------------------ | ------------ |
| Miguel  Llancao   | @Miguelito160  | mllancao@usm.cl          | 202630029-3  |
| Alejandro Muñoz   | @FlrMoka       | amunoznav@usm.cl         | 202630013-7  |
| Camila Aburto     | @cxtrasca      | caburto@usm.cl           | 202630008-0  |

## 📝 Descripción breve del proyecto

> Descripción breve
Este proyecto es un sistema de monitoreo continuo para lactantes basado en un ESP32, que usa un sensor MPU9250 para calcular la frecuencia respiratoria y un sensor de temperatura LM35 para medir la temperatura corporal del bebé.

Los datos sensados se envían vía WiFi a un servidor web alojado en Replit, donde se muestran en tiempo real en una página web y se generan alertas automáticas cuando la temperatura o la frecuencia respiratoria salen de los rangos normales para su edad.*

---

## 🎯 Objetivos

- Objetivo general:
  - Facilitar la monitorización de signos vitales en personas pertenecientes a infantes.
- Objetivos específicos:
  - Tener un aviso facil para saber si la temperatura de la persona está en el rango aceptable de temperaturas (Considerando su edad)
  - Para que los padres tengan un poco más de tranquilidad a la hora del horario de sueño.
---

## 🧩 Alcance del proyecto

> *Definir qué aspectos cubre el proyecto y qué queda fuera del alcance (limitaciones).*

---

## 🛠️ Tecnologías y herramientas utilizadas

- Lenguaje(s) de programación:
  - Ej: Python, C (arduino)
- Microcontroladores
  - Arduino UNO Q, Esp32 U
- Sensores LMT84LPM, MPU-92

---

## 🗂️ Estructura del repositorio

```
/PROY-2026-GRUPO-Grupo6
│
├── docs/               # Documentación general y reportes
├── src/                # Código fuente del proyecto
├── tests/              # Casos de prueba
├── Imagenes/ 
└── README.md           # Este archivo
```

---

## 🚀 Instrucciones de Instalacion y Uso


1. **Clonar el repositorio:** `git clone ...`
2. **Dependencias:** Listar qué librerías necesitan (ej: `pip install -r requirements.txt` o librerías de Arduino).
3. **Ejecución:** Cómo se corre el código principal.

---

## 📐 Diseño del Sistema
![Diagrama de Conexiones](.Imagenes/design.jpg)

-Imagen ilustrativa de como se vería las conexiónes de nuestro proyecto.

---

## 📅 Cronograma de trabajo

[Carta Gantt](https://usmcl-my.sharepoint.com/:x:/g/personal/cflorest_usm_cl/IQBMn-xOXonNRIqmBjaSvqLRAXTBRb4JK0oXyoDaD-OnSwc?e=4hwgP9)

---

## 📚 Bibliografía

Frecuencia respiratoria (respiraciones por minuto) en lactantes:

American Academy of Pediatrics. (s.f.). Fever and your baby. HealthyChildren.org. https://www.healthychildren.org/English/health-issues/conditions/fever/Pages/Fever-and-Your-Baby.aspx

Temperatura corporal en lactantes:

World Health Organization. (1997). Thermal protection of the newborn: A practical guide. WHO. https://www.who.int/publications/i/item/WHO-RHT-MSM-97-2

---

## 📌 Notas adicionales

>Conseguír Sensores Termicos y hacerlos funcionar con arduino. 
*Espacio para dejar cualquier comentario útil, como pendientes, acuerdos del grupo, consideraciones especiales, etc.*
