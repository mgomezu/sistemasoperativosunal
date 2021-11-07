import socket
import asyncio
import ssl

file = open("funciones.txt", "w")
host = "www.buda.com"
port = 443
context = ssl.create_default_context()

async def funcion1(tiempo):
    await asyncio.sleep(tiempo)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente = context.wrap_socket(cliente, server_hostname = host)
        cliente.connect ((host, port))
        cmd = "GET /api/v2/markets/btc-clp HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"
        cliente.send(cmd.encode())
        data = cliente.recv(50000).decode().split("\n")
        file.write(data.pop() + "\n")
        print() 

async def funcion2(tiempo):
    await asyncio.sleep(tiempo)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente = context.wrap_socket(cliente, server_hostname = host)
        cliente.connect ((host, port))
        cmd = "GET /api/v2/markets/btc-clp/volume HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"
        cliente.send(cmd.encode())
        data = cliente.recv(50000).decode().split("\n")
        file.write(data.pop() + "\n")

async def funcion3(tiempo):
    await asyncio.sleep(tiempo)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente = context.wrap_socket(cliente, server_hostname = host)
        cliente.connect ((host, port))
        cmd = "GET /api/v2/markets/btc-clp/ticker HTTP/1.0\r\nHost: www.buda.com\r\n\r\n"
        cliente.send(cmd.encode())
        data = cliente.recv(50000).decode().split("\n")
        file.write(data.pop() + "\n")

async def main():
    
    tasks = (funcion1(0), funcion2(1), funcion3(2))
    await asyncio.gather(*tasks)
    file.close()

asyncio.run(main())