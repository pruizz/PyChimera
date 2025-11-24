<div align="center">
# 🐍 PROJECT CHIMERA
### The Ultimate Python Black-Ops Toolkit

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/Interface-CustomTkinter-blueviolet?style=for-the-badge)
![Security](https://img.shields.io/badge/Focus-Offensive_Security-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

**Una implementación práctica de herramientas ofensivas desarrolladas íntegramente en Python.**  
*Proyecto Académico de Ciberseguridad & Hacking Ético*

[Ver Demo](#-demo) • [Instalación](#-instalación) • [Arsenal](#-arsenal-herramientas) • [Aviso Legal](#-aviso-legal)

</div>

---

## 📜 Descripción

**Project Chimera** es una suite modular diseñada para fines educativos que simula las 4 fases críticas de una operación ofensiva controlada. El objetivo pedagógico es ayudar a estudiantes y profesionales a comprender vectores de ataque, técnicas de defensa y mitigación en un entorno controlado y responsable.

Este repositorio contiene implementaciones de laboratorio y utilidades con interfaz gráfica (CustomTkinter) para facilitar prácticas, demostraciones y ejercicios de formación en ciberseguridad.

Nota: El contenido es de naturaleza dual (investigación/educativa). Su uso está estrictamente limitado a entornos de laboratorio, con permiso explícito y conforme a la legislación aplicable. Consulte el apartado "Aviso Legal" más abajo.

## ⚔️ Arsenal (Herramientas)

La suite "Quimera" está organizada en 4 módulos principales (correspondientes a fases de la kill-chain). A continuación se ofrece una visión general de cada módulo. Esta sección describe funcionalidades a alto nivel — no proporciona instrucciones operativas para actividades maliciosas.

| Fase (Kill Chain) | Módulo | Descripción (resumen) | Librerías clave |
| :--- | :--- | :--- | :--- |
| 1. RECON 👁️ | Bulk Geo-Tracker | Análisis forense masivo de metadatos EXIF en carpetas de imágenes. Genera visualizaciones HTML con mapas de calor y trazados GPS para análisis forense/privacidad. | Pillow, exifread, folium |
| 2. CRACKING 🔨 | Vault Breaker | Herramienta de fuerza bruta multihilo orientada a ejercicios de recuperación/recue. Permite evaluar la robustez de contraseñas en archivos protegidos (ZIP/PDF) en entornos de prueba. | zipfile, threading |
| 3. CRYPTO 🔐 | Ransomware Sim | Simulador de cifrado para uso pedagógico: cifra directorios en un entorno controlado para experimentar con detección y recuperación (soporte para algoritmos simétricos). NO es un malware operativo fuera de laboratorio. | cryptography |
| 4. ATTACK 💀 | C2 Commander | Framework de pruebas para entender comunicaciones cliente-servidor y telemetría remota en entornos controlados (p. ej. reverse shells de laboratorio y keylogging sólo para ejercicios con consentimiento). | socket, pynput |

> Importante: las implementaciones incluidas están pensadas para pruebas controladas y con fines educativos. Nunca las despliegue contra sistemas sin autorización.

## 📸 Demo

> Captura de ejemplo de la interfaz (placeholder).

![Interfaz Principal](https://via.placeholder.com/800x450?text=Project+Chimera+GUI+Screenshot)

## 🚀 Instalación

Siga estos pasos para preparar un entorno de desarrollo aislado. No ejecute herramientas de este repositorio en máquinas de producción ni contra sistemas ajenos.

1. Clonar el repositorio
```bash
git clone https://github.com/pruizz/Black-Ops-Toolkit.git
cd Black-Ops-Toolkit
```

2. Crear y activar un entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias (si existe requirements.txt)
```bash
pip install -r requirements.txt
```

4. Ejecutar la GUI (ejemplo)
- Abra una terminal en el directorio del proyecto y ejecute:
```bash
python main.py
```
Nota: main.py es un ejemplo; consulte la estructura del repo y ajuste según el módulo que vaya a probar. Siempre opere en entornos de laboratorio aislados.

## 📁 Estructura del proyecto

- /docs — Documentación adicional y guías de laboratorio (si está presente).
- /modules — Cada módulo (recon, cracking, crypto, attack) en su propio subdirectorio.
- main.py — Punto de entrada de la interfaz gráfica (si aplica).
- requirements.txt — Dependencias de Python.

(Ajuste según la estructura real del repositorio.)

## 🛡️ Aviso Legal y Ética (Obligatorio)

Este proyecto es exclusivamente para uso educativo, investigación y pruebas en entornos controlados. Cualquier uso de las herramientas aquí descritas para comprometer sistemas, datos o privacidad sin el permiso explícito del propietario constituye una actividad ilegal y está totalmente fuera del propósito de este repositorio.

Al utilizar este software usted:
- Declara y garantiza que tiene permiso expreso para realizar pruebas en los sistemas objetivo.
- Acepta no usar estas herramientas para actividades maliciosas o no autorizadas.
- Comprende que el autor no asume responsabilidad por el uso indebido del código.

Si su intención es practicar, hágalo en máquinas virtuales, laboratorios dedicados (p. ej. entornos CTF, máquinas de práctica) y con autorización.

## 🧭 Buenas prácticas de uso en laboratorio

- Aísle el entorno de pruebas (VMs, redes privadas).
- Mantenga snapshots/respaldos antes de ejecutar operaciones destructivas.
- Registre y documente las pruebas.
- Use cuentas y recursos de prueba, no datos reales de terceros.

## 🤝 Contribuciones

Si desea contribuir:
- Abra un issue describiendo la propuesta o corrección.
- Cree PRs pequeñas y enfocadas con tests/documentación.
- Respete el aviso legal y evite añadir instrucciones operativas que faciliten abuso.

Código malicioso o documentación que promueva actividades ilegales será rechazado.

## 📄 Licencia

Proyecto bajo licencia MIT. Consulte el archivo LICENSE para más detalles.

## 📬 Contacto

- Autor / Mantenedor: pruizz  
- Para consultas relacionadas con investigación/educación: abra un issue o contacte al mantenedor a través de GitHub.

---

Gracias por revisar Project Chimera. Use estas herramientas con responsabilidad y siempre dentro del marco legal y ético aplicable.
