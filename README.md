# PROY-2026-GRUPO6

Repositorio del grupo 6 para el proyecto del ramo *Proyecto Inicial (IWG400)* – 2026.

## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol USM      |
| ----------------- | -------------- | ------------------------ | ------------ |
| Miguel  Llancao   | @Miguelito160  | mllancao@usm.cl          | 202630029-3  |
| Alejandro Muñoz   | @FlrMoka       | amunoznav@usm.cl         | 202630013-7  |
| Camila Aburto     | @cxtrasca      | caburto@usm.cl           | 202630008-0  |

## 📝 Descripción breve del proyecto

> *Este proyecto es un sistema de monitoreo continuo para lactantes basado en un ESP32, que usa un sensor MPU9250 para calcular la frecuencia respiratoria y un sensor de temperatura LM35 para medir la temperatura corporal del bebé. Los datos sensados se envían vía WiFi a un servidor web alojado en Replit, donde se muestran en tiempo real en una página web y se generan alertas automáticas cuando la temperatura o la frecuencia respiratoria salen de los rangos normales para su edad.*

---

## 🎯 Objetivos

**Objetivo general:**

* Facilitar la monitorización de signos vitales (temperatura corporal y frecuencia respiratoria) en lactantes, mediante un sistema electrónico de bajo costo que permita a los padres o cuidadores supervisar su estado de salud de forma remota y en tiempo real.

**Objetivos específicos:**

* Diseñar un sistema de adquisición de datos basado en ESP32 capaz de medir la temperatura corporal y la frecuencia respiratoria del lactante mediante sensores LM35 y MPU9250.

* Implementar un mecanismo de alerta visual/web que notifique de forma clara y sencilla cuando los valores medidos se encuentren fuera de los rangos normales considerados según la edad del lactante.

* Transmitir los datos sensados de forma inalámbrica a un servidor web, permitiendo su visualización en tiempo real desde cualquier dispositivo con acceso a internet.

* Brindar mayor tranquilidad a los padres durante el horario de sueño del bebé, al contar con un monitoreo continuo y automatizado que reduzca la necesidad de supervisión constante y manual.
---

## 🧩 Alcance del proyecto

> *Definir qué aspectos cubre el proyecto y qué queda fuera del alcance (limitaciones).*

---

## 🛠️ Tecnologías y herramientas utilizadas

- Lenguaje(s) de programación:
  - Ej: Python, C (arduino)
- Microcontroladores
  - Arduino UNO Q, Esp32 U
- Sensores LM35, MPU-9250

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
![Diagrama de Conexiones](Transmisor.png)

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
