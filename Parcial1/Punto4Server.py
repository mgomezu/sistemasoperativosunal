import socket
import os
import shutil

host = socket.gethostname() 
port = 12345
BUFFER_SIZE = 1024

lista_archivos = os.getcwd() + '\ArchivosPunto4'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host, port)) 
    socket_tcp.listen(5) 
    conn, addr = socket_tcp.accept() 
    with conn:        
        try:
            input_data = conn.recv(BUFFER_SIZE)
        except error:
            print("Error de lectura.")
            socket_tcp.close()
        else:
            if input_data:
                if isinstance(input_data, bytes):
                    end = input_data[0] == 1
                else:
                    end = input_data == chr(1)
                if not end:
                    input_data = input_data.decode()
                    input_data = input_data.split(sep='.txt', maxsplit=2)
                    f = open("ArchivosPunto4/"+input_data[0]+'.txt', "w")
                    f.write(input_data[1])
                else:
                    print("El archivo se ha recibido correctamente.")
                    contenido = os.listdir(lista_archivos)
                    conn.send(contenido.encode())
                    f.close()
        print("El archivo se ha recibido correctamente.")
        contenido = os.listdir(lista_archivos)
        conn.send(str(contenido).encode('utf-8'))
