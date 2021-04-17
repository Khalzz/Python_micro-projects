import random #en este caso me agrega la opcion de dar un numero de forma aleatoria (random.randint(rango de numeros ej 1,6))
import time #en este caso me agrega la opcion de esperar antes de dar la siguiente linea (time.sleep("tiempo en seg"))
import getpass #en este caso me agrega la opcion de con "getpass.getpass() el que no se muestre lo escrito en consola"

#variables
menujug = "1) un jugador \n2) dos jugadores"
menudif = "1) quiero ser el mejor >:D!!! \n2) quiero azar pero que sea justo \n3) quiero ser destruido BRUTALEMTE!!!"
eleccion = "1) piedra \n2) papel \n3) tijeras"

#menu
print("Hola!! bienvenido a mi Piedra, Papel o Tijeras, diviertete!!! :D")
print(menujug)
players = int(input("selecciona el numero de jugadores: "))
if players == 1:

    #modo de 1 jugador
    print("has seleccionado 1 jugador")
    print(menudif)
    dif = int(input("selecciona la dificultad: "))

    #dificultades
    if dif == 1:

        #facil
        print("has seleccionado la dificultad facil")
        print(eleccion)
        tu = int(input("la maquina esta haciendo su eleccion, elige la tuya!!: "))

        if tu == 1:
            #piedra 
            print ("la maquina ha elegido...")
            time.sleep(3)
            print ("tijeras")
            time.sleep(1)
            print ("GANASTE!!! felicidades :D")
            input()
            
        elif tu == 2:
            #papel
            print ("la maquina ha elegido...")
            time.sleep(3)
            print ("piedra")
            time.sleep(1)
            print ("GANASTE!!! felicidades :D")
            input()
            
        elif tu == 3:
            #tijera    
            print ("la maquina ha elegido...")
            time.sleep(3)
            print ("papel")
            time.sleep(1)
            print ("GANASTE!!! felicidades :D")
            input() 
             
        else:
            print("esa no es una opcion valida!!!")
            input()

    if dif == 2:
        
        #media    
        print("has seleccionado la dificultad media")
        print(eleccion)
        pc = random.randint(0,2)
        tu = int(input("la maquina esta haciendo su eleccion, elige la tuya!!: "))
        
        
        if (tu == 1):
            #piedra    
            if (pc == 0):
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("piedra")
                time.sleep(1)
                print ("empate!!!")
                input() 

            elif (pc == 1):
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("papel")
                time.sleep(1)
                print ("perdiste")
                input()

            elif (pc == 2):
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("tijeras")
                time.sleep(1)
                print ("GANASTE!!! felicidades :D")
                input() 

        elif (tu == 2):
            #papel    
            if (pc == 0):
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("piedra")
                time.sleep(1)
                print ("GANASTE!!! felicidades :D")
                input() 

            elif (pc == 1):     
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("papel")
                time.sleep(1)
                print ("empate!!!")
                input() 

            elif (pc == 2):
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("tijeras")
                time.sleep(1)
                print ("perdiste")
                input() 

        elif (tu == 3):
            #tijeras    
            if (pc == 0):
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("piedra")
                time.sleep(1)
                print ("perdiste")
                input() 

            elif (pc == 1):     
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("papel")
                time.sleep(1)
                print ("GANASTE!!! felicidades :D")
                input() 

            elif (pc == 2):
                print ("la maquina ha elegido...")
                time.sleep(3)
                print ("tijeras")
                time.sleep(1)
                print ("empate!!!")
                input()    
        else:
            print("esa no es una opcion valida!!!")   
             
    if dif == 3: 
        #dificil    
        print("has decidido jugar el modo imposible")
        print("aviso importante: este modo de juego es IMPOSIBLE!!! de ganar")
        print(eleccion)
        tu = int(input("la maquina esta haciendo su eleccion, elige la tuya!!: "))

        if tu == 1:
            #piedra 
            print ("la maquina ha elegido...")
            time.sleep(3)
            print ("papel")
            time.sleep(1)
            print ("oh, que pena, PERDISTE!!! :) ")
            input()

        elif tu == 2:
            #papel
            print ("la maquina ha elegido...")
            time.sleep(3)
            print ("tijeras")
            time.sleep(1)
            print ("oh, que pena, PERDISTE!!! :) ")
            input()

        elif tu == 3:
            #tijera    
            print ("la maquina ha elegido...")
            time.sleep(3)
            print ("piedra")
            time.sleep(1)
            print ("oh, que pena, PERDISTE!!! :) ")
            input() 

        else:
            print("esa no es una opcion valida!!!")
            input()

#modo de 2 jugadores
elif players == 2:
    print("has seleccionado 2 jugadores")
    print(eleccion)
    jug1 = int(getpass.getpass("turno de jugador 1: "))
    jug2 = int(getpass.getpass("turno de jugador 2: "))

    if (jug1 == 1):
        #piedra    
        if (jug2 == 1):
            time.sleep(3)
            print("EMPATE!!!")
            
        elif (jug2 == 2):
            time.sleep(1)
            print("el ganador es")
            time.sleep(1)
            print("el jugador 2!!!!")
            
        elif (jug2 == 3):
            time.sleep(1)
            print("el ganador es")
            time.sleep(1)
            print("el jugador 1!!!!") 

    elif (jug1 == 2):
        #papel    
        if (jug2 == 2):
            time.sleep(3)
            print("EMPATE!!!")
            
        elif (jug2 == 3):
            time.sleep(1)
            print("el ganador es")
            time.sleep(1)
            print("el jugador 2!!!!")
            
        elif (jug2 == 1):
            time.sleep(1)
            print("el ganador es")
            time.sleep(1)
            print("el jugador 1!!!!")

    elif (jug1 == 3):
        #tijeras    
        if (jug2 == 3):
            time.sleep(3)
            print("EMPATE!!!")
            
        elif (jug2 == 1):
            time.sleep(1)
            print("el ganador es")
            time.sleep(1)
            print("el jugador 2!!!!")
            
        elif (jug2 == 2):
            time.sleep(1)
            print("el ganador es")
            time.sleep(1)
            print("el jugador 1!!!!") 
                   
else:
    print("esa no es una opcion valida")
    input()
