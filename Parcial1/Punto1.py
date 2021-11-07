import os
import pandas as pd
from pandas import ExcelWriter


def writeTXT(funciones):
    escritura = open("Archivo.txt", "w")
    escritura.writelines("Funciones:\n")
    while len(funciones)!=0:
        escritura.writelines(funciones.pop() +"\n")
    escritura.close()

def writeExcel(funciones):
    df = pd.DataFrame({'funciones': funciones})
    df = df[['funciones']]
    writer = ExcelWriter('archivo.xlsx')
    df.to_excel(writer, 'Hoja de datos', index=False)
    writer.save()


def main():
    funcion1 = "Permitir que se instale el software. "
    funcion2 = "Actuar como una interfaz entre el hardware del computador y el usuario "
    funcion3 = "Gestionar el Hardware "
    funcion4 = "Administrar los recursos "
    funcion5 = "Facilitar el trabajo del usuario "
    funciones = [funcion1, funcion2, funcion3, funcion4, funcion5]
    writeTXT(funciones)
    writeExcel(funciones)

main()

