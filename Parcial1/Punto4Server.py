import socket
import os
import shutil

host = socket.gethostname() 
port = 12345
BUFFER_SIZE = 1024
lista_archivos = "lista_archivos.txt"
f = open('lista_archivos.txt','a')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host, port)) 
    socket_tcp.listen(1) 
    conn, addr = socket_tcp.accept() 
    with conn:
        print("Conexion establecida") 
        data = conn.recv(BUFFER_SIZE)
        if not data:
            f.close()
            conn.send("error al enviar archivo".encode())
            conn.close()
        else:
            ruta = os.getcwd() + os.sep
            origen = ruta + data.decode('utf-8')
            destino = ruta + 'ArchivosPunto4//' + data.decode('utf-8')
            shutil.copy(origen, destino)
            f.write(data.decode('utf-8') + '\n')  
        f.close()
        conn.send(lista_archivos.encode())
        conn.close()