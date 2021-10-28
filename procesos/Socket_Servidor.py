import socket
import sys


host = socket.gethostname() 
port = 12345
BUFFER_SIZE = 1024 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host, port)) 
    socket_tcp.listen(5) 
    conn, addr = socket_tcp.accept() 
    with conn:
        print("Conexion establecida") 
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            else:
                saludo = '{}'.format(data.decode('utf-8'))
                if saludo ==  "Hola":
                    print ("!Hola mundo!")
                else:
                    print ("Saluda primero")
            conn.send(data)