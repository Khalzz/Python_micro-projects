
import shutil #nos permite interactuar con carpetas de forma avanzada
import time

ruta ='ingresa/la/carpeta/a/copiar'
rutaCopia ='ingresa/la/carpeta/donde/ira/el/respaldo'

time.sleep(0.3)
print("Eliminando carpeta original")
shutil.rmtree(rutaCopia)
print("La carpeta original se ha eliminado")

time.sleep(0.3)
print("Se esta generando el respaldo")
shutil.copytree(ruta,rutaCopia)
print("Finalizado")
