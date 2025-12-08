import os
import zipfile
import time
import zlib

DICT_DEFAULT = "dict.txt"

def crack_zip(zip_path,dict_path = DICT_DEFAULT):
    
    if not os.path.exists(zip_path):
        return "Error: El archivo ZIP no existe"

    if not os.path.exists(dict_path):
        return "Error: El Diccionario no existe"
    
    print(f"[*] Iniciando ataque sobre: {os.path.basename(zip_path)}")

    try:
        #Creamos el objeto de tipo zipFile
        zf = zipfile.ZipFile(zip_path)

        # Verificamos que el ZIP no esté vacío
        if len(zf.namelist()) == 0:
            return "[-] Error: El archivo ZIP está vacío."
        
        # Seleccionamos el primer archivo del ZIP para poder ver si al poner la contraeña correcta se muestra algo
        target_file = zf.namelist()[0]

    except zipfile.BadZipFile:
        return "Error: El archivo no es un ZIP válido."
    
    try:
        with open(dict_path, "r", encoding="utf-8", errors="ignore") as f:
            wordlist = f.readlines()
    except Exception as e:
        return f"[-] Error de lectura I/O: {str(e)}"
    

    total_passwords = len(wordlist)
    print(f"\n[*] INICIANDO ATAQUE DE DICCIONARIO ({total_passwords} palabras)...")
    print("-" * 40)

    start_time = time.time()
    attempts = 0
    password_found = None

    for pwd in wordlist:
        attempts += 1
        password = pwd.strip()
        password_bytes = password.encode('utf-8')

        try:
            #El read si no la conttraseña no es valida lanza una excepcion a si que si se ejecuta corerctamente si se guarda la contraseña si no se rompe
            print(f" >> Probando clave [{attempts}/{total_passwords}]: {password}", end='\r')
            time.sleep(0.05)
            zf.read(target_file,pwd = password_bytes)
            password_found = password
            print(f"\n\n[+] ¡MATCH CONFIRMADO! 🔓")
            break
    
        except (RuntimeError, zipfile.BadZipFile, zlib.error):
            # RuntimeError: Contraseña incorrecta
            # BadZipFile: Error CRC
            pass
        except Exception:
            # Ignoramos excepciones diferentes para no detener el ataque
            pass
    
    zf.close()
    duration = time.time() - start_time
    if password_found:
        return (f"✅ ¡CONTRASEÑA ENCONTRADA!\n"
                f"--------------------------\n"
                f"🔑 Clave: '{password_found}'\n"
                f"📊 Intentos: {attempts}\n"
                f"⏱ Tiempo: {duration:.2f} segundos")
    else:
        return (f"❌ ATAQUE FALLIDO\n"
                f"Se probaron {attempts} contraseñas y ninguna funcionó.\n"
                f"Prueba con un diccionario más completo.")