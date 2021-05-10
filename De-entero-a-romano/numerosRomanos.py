from os import system

system('cls')

valor1 = 'I'
valor4 = 'IV'
valor5 = 'V'
valor9 = 'IX'
valor10 = 'X'
valor40 = 'XL'
valor50 = 'L'
valor90 = 'XC'
valor100 = 'C'
valor400 = 'CD'
valor500 = 'D'
valor900 = 'CM'
valor1000 = 'M'

n = int(input("Ingresa un numero entre el 1 y el 3000: "))

milesima = ''
centesima500 = ''
centesima = ''
decima50 = ''
decima = ''
unidad = ''


# antes de continuar con el código debes tomar en cuenta que este fue diseñado para "transformar enteros en numeros romanos"
# pero sin utilizar nada mas que condicionales basicas (if, elif, else) en lugar de bucles
if (n > 0 and n <= 3000):
    if (n >= 1000 and n <= 3000):
        if (n >= 1000 and n < 2000):
            milesima = valor1000
            n -= 1000
        if (n >= 2000 and n < 3000):
            milesima = valor1000*2
            n -= 2000
        if (n == 3000):
            milesima = valor1000*3
            n -= 3000

    if (n >= 900 and n < 1000):
        centesima500 = valor900
        n -= 900

    if (n >= 500 and n < 900):
        centesima500 = valor500
        n -= 500

    if (n >= 100 and n < 500):
        if (n >= 100 and n < 200):
            centesima = valor100
            n -= 100
        elif (n >= 200 and n < 300):
            centesima = valor100*2
            n -= 200
        elif (n >= 300 and n < 400):
            centesima = valor100*3
            n -= 300
        elif (n >= 400 and n < 500):
            centesima = valor400
            n -= 400

    if (n >= 90 and n < 100):
        decima50 = valor90
        n -= 90

    if (n >= 50 and n < 90):
        decima50 = valor50
        n -= 50

    if  (n > 0 and n < 50):
        if (n >= 10 and n < 20):
            decima = valor10
            n -= 10
        elif (n >= 20 and n < 30):
            decima = valor10*2
            n -= 20
        elif (n >= 30 and n < 40):
            decima = valor10*3
            n -= 30
        elif (n >= 40 and n < 50):
            decima = valor40
            n -= 40

    if (n > 0 and n < 10):
        if (n > 0 and n < 4):
            unidad = valor1 * n
            n -= n
        elif (n == 4):
            unidad = valor4
            n -= n
        elif (n > 4 and n < 9):
            unidad = valor5 + valor1 * (n-5)
            n -= n
        elif (n == 9):
            unidad = valor9
            n -= n
else:
    print('Valor invalido!!!!')

if (n == 0):
    print(milesima + centesima500 + centesima + decima50 + decima + unidad)
    print('Terminado')