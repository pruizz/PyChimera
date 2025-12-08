import os
from cryptography.fernet import Fernet

# Nombre del archivo donde se guardará la llave de desencriptado
ARCHIVO_KEY = "master.key"

def generate_key():
    if not os.path.exists(ARCHIVO_KEY):
        key = Fernet.generate_key()
        with open(ARCHIVO_KEY, "wb") as k:
            k.write(key)
        return key
    else:
        with open(ARCHIVO_KEY, "rb") as k:
            return k.read()