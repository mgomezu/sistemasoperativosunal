import asyncio
import time

start = time.time()
archivo = "Archivo.txt"
async def async_sleep(a):
    await asyncio.sleep(a)

async def write(a):
    await async_sleep(a)
    escritura = open(archivo, "w")
    escritura.writelines("Hello")
    escritura.close()

async def read(a):
    await async_sleep(a)
    lectura = open(archivo, "r")
    content = lectura.read()
    print(content)
    lectura.close()

async def files(a):
    await async_sleep(a)
    resultado = open(archivo, "a")
    resultado.write(" world")
    resultado.close()

async def main():
    tasks = (write(1), files(2), read(1), read(2))
    await asyncio.gather(*tasks)
    print(f"Completed after: {time.time() - start}")

asyncio.run(main())



