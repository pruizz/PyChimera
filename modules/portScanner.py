import socket
import threading
from queue import Queue

#"Este módulo implementa un modelo de productor-consumidor utilizando concurrencia (threading) para optimizar la velocidad del escaneo. 
# Funciona inicializando una Cola (Queue) sincronizada que el hilo principal llena con todos los puertos objetivo. 
# Simultáneamente, se ejecutan 100 hilos 'trabajadores' en paralelo que consumen tareas de esa cola: 
# cada hilo extrae un puerto, intenta establecer la conexión socket, y notifica la finalización con task_done(). 
# El método crítico es q.join(), que bloquea la ejecución del programa principal obligándolo a esperar hasta que el contador de tareas pendientes llegue a cero, 
# garantizando así que todos los puertos hayan sido procesados antes de mostrar los resultados finales."
# Lista de puertos comunes
COMMON_PORTS = {
    20: "FTP-Data", 21: "FTP", 22: "SSH", 23: "TELNET", 
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 
    135: "RPC", 139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 
    445: "SMB", 993: "IMAP-SSL", 995: "POP3-SSL", 
    1433: "MSSQL", 3306: "MySQL", 3389: "RDP", 
    5900: "VNC", 8080: "HTTP-Proxy",4444: "METASPLOIT/C2"
}

socket.setdefaulttimeout(1) 

def port_scan(target, port, res):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = s.connect_ex((target, port)) #Devuelve 0 si el puerto esta abierto
        
        if res == 0:
            servicio = COMMON_PORTS.get(port, "Unknown")
            info = f"[+] PUERTO {port:<5} ABIERTO  -->  {servicio}"
            res.append(info)
        s.close()
    except:
        pass

def threader(target, q, res):
    #Funcion de los hilos
    while True:
        worker = q.get()
        port_scan(target, worker, res)
        q.task_done()

def escanear_objetivo(ip_objetivo):
    results = [] 
    
    print(f"[*] Iniciando escaneo en: {ip_objetivo}")
    q = Queue()
    
    # Creamos 100 hilos simultaneos
    for _ in range(100):
        # Asociamos a cada thread la funcion que escanea el puerto y le mandamos los parametros
        t = threading.Thread(target=threader, args=(ip_objetivo, q, results))
        t.daemon = True
        t.start()
    
    #Llenamos la cola con por puertos mas comunes
    for worker in range(1, 1025):
        q.put(worker)
    
    for p in COMMON_PORTS: #Añadimos el resto mayores de 1024 que son los mas comunes
        if p > 1024:
            q.put(p)
            
    q.join() #Esperamos a que todos los hilos acaben
    
    # Si hay resultados
    if results:
        # Ordenamos por número de puerto
        results.sort(key=lambda x: int(x.split()[2]))
        return "\n".join(results)
    else:
        return "[-] No se encontraron puertos abiertos."

