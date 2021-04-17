import random

#advertencia, no funciona al 100% ni en el 100% de los compiladores
#recomiendo usar compiladores en linea pues asi el procesamiento no lo hace nuestro equipo
#la pagina que uso para este codigo es https://repl.it/languages/python3

def conteo(n):
    #se define el numero basico de cada caso
    numerosCirculo = 0
    numerosTotales = 0
    #por cada numero en el rango que creemos en la funcion
    for i in range(n):
        #se hace un calculo de float aleatorio entre 0 y 1 para x e y
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        #la distancia entre el 0 y el punto dado anteriormente es sacado con la sig formula
        distancia = x**2 + y**2
        if distancia <= 1:
            numerosCirculo += 1
        numerosTotales += 1
    return 4*(numerosCirculo/numerosTotales)

#para correrlo debes escribir en el compilador conteo(numero de intentos) por ejemplo conteo(100)
