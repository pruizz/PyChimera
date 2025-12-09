<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/Interface-CustomTkinter-blueviolet?style=for-the-badge)
![Security](https://img.shields.io/badge/Focus-Offensive_Security-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

<h1 align="center">🐍 PROJECT CHIMERA</h1>
<h3 align="center">The Ultimate Python Black-Ops Toolkit</h3>

<p align="center">
<strong>Una implementación práctica de herramientas ofensivas desarrolladas íntegramente en Python.</strong><br>
<em>Proyecto Académico de Ciberseguridad & Hacking Ético</em>
</p>

<p align="center">
<a href="#-demo">Ver Demo</a> • <a href="#-instalación">Instalación</a> • <a href="#-arsenal-herramientas">Arsenal</a> • <a href="#-aviso-legal">Aviso Legal</a>
</p>

---

## 📜 Descripción

**Project Chimera** es una suite modular diseñada para fines educativos que simula las 4 fases críticas de una operación ofensiva controlada. El objetivo pedagógico es ayudar a estudiantes y profesionales a comprender metodologías, técnicas y contramedidas en un contexto de laboratorio seguro.

Este repositorio contiene implementaciones de laboratorio y utilidades con interfaz gráfica (CustomTkinter) para facilitar prácticas, demostraciones y ejercicios de formación en ciberseguridad.

**Nota:** El contenido es de naturaleza dual (investigación/educativa). Su uso está estrictamente limitado a entornos de laboratorio, con permiso explícito y conforme a la legislación aplicable. Consulte siempre las leyes locales antes de realizar pruebas de penetración.

## ⚔️ Arsenal (Herramientas)

La suite "Quimera" está organizada en 4 módulos principales (correspondientes a fases de la kill-chain). A continuación se ofrece una visión general de cada módulo. Esta sección describe funcionalidades implementadas o en desarrollo para fines exclusivamente didácticos.

| Fase (Kill Chain) | Módulo | Descripción (resumen) | Librerías clave |
|:------------------|:-------|:----------------------|:----------------|
| 1. RECON 👁️ | Bulk Geo-Tracker | Análisis forense masivo de metadatos EXIF en carpetas de imágenes. Genera visualizaciones HTML con mapas de calor y trazados GPS para análisis forense/privacidad. | `Pillow`, `folium`, `os`, `webbrowser` |
| 2. CRACKING 🔨 | Vault Breaker | Herramienta de fuerza bruta orientada a ejercicios de recuperación/rescate. Permite evaluar la robustez de contraseñas en archivos protegidos (ZIP) mediante ataque de diccionario en entornos de laboratorio. | `zipfile`, `zlib`, `os`, `time` |
| 3. NETWORK 📡 | Port Scanner | Escáner de puertos multihilo que implementa el patrón productor-consumidor. Detecta servicios vulnerables y puertos abiertos usando 100 hilos concurrentes para optimizar la velocidad del escaneo. | `socket`, `threading`, `queue` |
| 4. ATTACK 💀 | C2 Commander | Framework de pruebas para entender comunicaciones cliente-servidor y telemetría remota en entornos controlados (p. ej. reverse shells de laboratorio y keylogging sólo en VMs autorizadas). | `socket`, `pynput`, `subprocess`, `threading`, `os` |

> **Importante:** las implementaciones incluidas están pensadas para pruebas controladas y con fines educativos. Nunca las despliegue contra sistemas sin autorización.

## 📸 Demo

> Captura de ejemplo de la interfaz (placeholder).

<div align="center">

![Interfaz Principal](https://via.placeholder.com/800x450?text=Project+Chimera+GUI+Screenshot)

</div>

## 🚀 Instalación

Siga estos pasos para preparar un entorno de desarrollo aislado. **No ejecute herramientas de este repositorio en máquinas de producción ni contra sistemas ajenos.**

### 1. Clonar el repositorio

```bash
git clone https://github.com/pruizz/PyChimera.git
cd PyChimera
```

### 2. Crear y activar un entorno virtual (recomendado)

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la GUI

Abra una terminal en el directorio del proyecto y ejecute:

```bash
python main.py
```

> **Nota:** `main.py` es un ejemplo; consulte la estructura del repo y ajuste según el módulo que vaya a probar. Siempre opere en entornos de laboratorio aislados.

## 📁 Estructura del proyecto

```
PyChimera/
├── modules/           # Módulos de herramientas de seguridad
│   ├── recon.py       # Análisis de metadatos EXIF y geolocalización
│   ├── zipCracker.py  # Cracking de archivos ZIP
│   ├── portScanner.py # Escáner de puertos multihilo
│   ├── payload.py     # Payload con keylogger y reverse shell
│   └── server.py      # Servidor C2 para comunicación con payload
├── main.py            # Punto de entrada de la interfaz gráfica
├── requirements.txt   # Dependencias de Python
└── README.md          # Este archivo
```

## 🛡️ Aviso Legal y Ética (Obligatorio)

Este proyecto es **exclusivamente para uso educativo, investigación y pruebas en entornos controlados**. Cualquier uso de las herramientas aquí descritas para comprometer sistemas, datos o privacidad sin autorización expresa es **ilegal** y está **estrictamente prohibido**.

### Al utilizar este software usted:

- ✅ Declara y garantiza que tiene **permiso expreso** para realizar pruebas en los sistemas objetivo.
- ✅ Acepta **no usar** estas herramientas para actividades maliciosas o no autorizadas.
- ✅ Comprende que el autor **no asume responsabilidad** por el uso indebido del código.

**Si su intención es practicar**, hágalo en máquinas virtuales, laboratorios dedicados (p. ej. entornos CTF, máquinas de práctica) y con autorización.

## 🧭 Buenas prácticas de uso en laboratorio

- 🔒 **Aísle el entorno de pruebas** (VMs, redes privadas).
- 💾 **Mantenga snapshots/respaldos** antes de ejecutar operaciones destructivas.
- 📝 **Registre y documente** las pruebas.
- 🚫 **Use cuentas y recursos de prueba**, no datos reales de terceros.

## 🤝 Contribuciones

Si desea contribuir:

1. Abra un **issue** describiendo la propuesta o corrección.
2. Cree **PRs pequeñas y enfocadas** con tests/documentación.
3. **Respete el aviso legal** y evite añadir instrucciones operativas que faciliten abuso.

⚠️ Código malicioso o documentación que promueva actividades ilegales será **rechazado**.

## 📄 Licencia

Proyecto bajo licencia **MIT**. Consulte el archivo [LICENSE](LICENSE) para más detalles.

## 📬 Contacto

- **Autor / Mantenedor:** [@pruizz](https://github.com/pruizz)
- Para consultas relacionadas con investigación/educación: abra un **issue** o contacte al mantenedor a través de GitHub.

---

<p align="center">
<strong>Gracias por revisar Project Chimera.</strong><br>
Use estas herramientas con responsabilidad y siempre dentro del marco legal y ético aplicable.
</p>
