import socket
import threading
from queue import Queue #Cola espcial de Thread Modelo Prodcutor Consumidor

# Lista de puertos comunes
COMMON_PORTS = {
    20: "FTP-Data", 21: "FTP", 22: "SSH", 23: "TELNET", 
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 
    135: "RPC", 139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 
    445: "SMB", 993: "IMAP-SSL", 995: "POP3-SSL", 
    1433: "MSSQL", 3306: "MySQL", 3389: "RDP", 
    5900: "VNC", 8080: "HTTP-Proxy", 4444: "METASPLOIT/C2"
}

socket.setdefaulttimeout(1) # Un segundo es suficiente para redes normales

def port_scan(target, port, res_list):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #
        res_conex = s.connect_ex((target, port)) 
        
        if res_conex == 0:
            servicio = COMMON_PORTS.get(port, "Unknown")
            info = f"[+] PUERTO {port:<5} ABIERTO  -->  {servicio}"
            
            res_list.append(info)
        s.close()
    except:
        pass

def threader(target, q, res_list):
    while True:
        worker = q.get()
        port_scan(target, worker, res_list)
        q.task_done()

def scan_obj(ip_attack):
    results = [] 
    
    print(f"[*] Iniciando escaneo en: {ip_attack}")
    q = Queue()
    
    # Creamos 100 hilos simultáneos
    for _ in range(100):
        t = threading.Thread(target=threader, args=(ip_attack, q, results))
        t.daemon = True
        t.start()
    
    # Llenamos la cola con puertos del 1 al 1024
    for worker in range(1, 1025):
        q.put(worker)
    
    # Añadimos puertos comunes altos
    for p in COMMON_PORTS:
        if p > 1024:
            q.put(p)
            
    q.join()
    
    # Procesar resultados
    if results:
        results = list(set(results))
        try:
            results.sort(key=lambda x: int(x.split()[2]))
        except:
            pass
        return "\n".join(results)
    else:
        return "[-] No se encontraron puertos abiertos."

