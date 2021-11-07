import socket
import asyncio

host = socket.gethostname()
port = 12345
BUFFER_SIZE = 1024
FILE = "ejemploPunto4.txt"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port))
    socket_tcp.send(FILE.encode())
    data = socket_tcp.recv(BUFFER_SIZE)
    f = open (data.decode('utf-8'),'r')
    mensaje = f.read()
    print(mensaje)
    f.close()