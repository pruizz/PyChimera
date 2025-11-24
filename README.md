<div align="center">
# 🐍 PROJECT CHIMERA
### The Ultimate Python Black-Ops Toolkit

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/Interface-CustomTkinter-blueviolet?style=for-the-badge)
![Security](https://img.shields.io/badge/Focus-Offensive_Security-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

**Una implementación práctica de herramientas ofensivas desarrolladas íntegramente en Python.**
<br>
*Proyecto Académico de Ciberseguridad & Hacking Ético*

[Ver Demo](#-demo) • [Instalación](#-instalación) • [Arsenal](#-arsenal-herramientas) • [Aviso Legal](#-aviso-legal)

</div>

---

## 📜 Descripción

**Project Chimera** es una suite modular de ciberseguridad diseñada para simular las 4 fases críticas de un ciberataque real. El objetivo pedagógico es comprender los vectores de ataque (Redes, Criptografía, Forense y Sistemas) para diseñar mejores defensas.

A diferencia de los scripts de consola tradicionales, Chimera cuenta con una **Interfaz Gráfica (GUI) moderna** basada en `CustomTkinter`, ofreciendo un panel de control centralizado para todas las operaciones.

## ⚔️ Arsenal (Herramientas)

La suite "Quimera" combina 4 cabezas (módulos) distintas:

| Fase (Kill Chain) | Módulo | Descripción Técnica | Librerías Clave |
| :--- | :--- | :--- | :--- |
| **1. RECON** 👁️ | **Bulk Geo-Tracker** | Análisis forense masivo de metadatos EXIF en carpetas de imágenes. Genera mapas de calor HTML interactivos para trazar rutas GPS de objetivos. | `Pillow`, `Folium` |
| **2. CRACKING** 🔨 | **Vault Breaker** | Herramienta de fuerza bruta multihilo para la rotura de seguridad en archivos comprimidos (ZIP/PDF) protegidos por contraseña. | `zipfile`, `threading` |
| **3. CRYPTO** 🔐 | **Ransomware Sim** | Simulador de malware que cifra directorios completos con algoritmo militar **AES-128**, renombra extensiones y modifica el fondo de escritorio. | `cryptography`, `ctypes` |
| **4. ATTACK** 💀 | **C2 Commander** | Servidor de Comando y Control (Reverse Shell) que permite ejecución remota de comandos y cuenta con un **Keylogger** en tiempo real. | `socket`, `pynput` |

## 📸 Demo

> *[INSERTA AQUÍ UNA CAPTURA DE TU INTERFAZ]*
> ![Interfaz Principal](https://via.placeholder.com/800x450?text=Project+Chimera+GUI+Screenshot)

## 🚀 Instalación

Sigue estos pasos para desplegar el entorno de desarrollo en tu máquina local:

### 1. Clonar el repositorio
bash
git clone [https://github.com/TU_USUARIO/project-chimera.git](https://github.com/TU_USUARIO/project-chimera.git)
cd project-chimera

### 2. Crear entorno virtual (Recomendado)
Para mantener las librerías aisladas y evitar conflictos:

bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
