"""
La función de este proyecto es hacer una multiplicación
efectivamente sin utilizar el operador '*'
sip, era totalmente necesario, no me juzguen
"""

numeroBoomer = int(input("¿que numero usaras como base? "))
numeroBase = numeroBoomer
multiplicador = int(input("¿que multiplicador usaras? "))

def multiplicar(boomer, base, mult):
    for i in range(1,mult):
        base = base + boomer
    print("tu resultado es: ", base);
    
multiplicar(numeroBoomer, numeroBase, multiplicador)