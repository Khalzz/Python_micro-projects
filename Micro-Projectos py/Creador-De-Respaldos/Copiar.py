import shutil #nos permite interactuar con carpetas de forma avanzada
import os
import time

ruta ='/home/khals/Desktop/ProjectAlone'
rutaCopia = '/home/khals/Desktop/DevShit/Respaldo'

def crearCarpeta():
    time.sleep(0.3)
    print("Eliminando carpeta original")
    shutil.rmtree(rutaCopia)
    print("La carpeta original se ha eliminado")
    time.sleep(0.3)
    print("Se esta generando el respaldo")
    shutil.copytree(ruta,rutaCopia)
    print("Finalizado")

if os.path.isdir(rutaCopia): #si existe carpeta "ruta copia" crear respaldo
    crearCarpeta()
else: #si la carpeta no existe, crear carpeta y hacer respaldo
    os.mkdir(rutaCopia)
    crearCarpeta()
