import socket
import asyncio
import os

host = socket.gethostname()
port = 12345
BUFFER_SIZE = 1024
archivo = "ejemploPunto4.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port))
    while True:
        f = open(archivo, "rb")
        content = archivo.encode() + f.read(BUFFER_SIZE)
        while content:
            socket_tcp.send(content)
            content = f.read(BUFFER_SIZE)
        break
    try:
        socket_tcp.send(chr(1))

    except TypeError:
        socket_tcp.send(bytes(chr(1), "utf-8"))
        
    f.close()
    print("El archivo ha sido enviado correctamente.")
    data = socket_tcp.recv(BUFFER_SIZE)
    print(data.decode())
    socket_tcp.close()

