#Funciones comprobar si un número cae en un rango determinado.

def Rango_Determinado(numero, rangoI, rangoF):
    rango = numero

    if numero > rangoI and numero < rangoF:
        print("El numero ingresado si esta en el rango establecido: ", rango)

    if numero == rangoI and numero < rangoF:
        print("El numero ingresado si esta en el rango establecido: ", rango)

    if numero > rangoI and numero == rangoF:
        print("El numero ingresado si esta en el rango establecido: ", rango)

    if numero < rangoI and numero < rangoF:
        print("El numero ingresado no esta en el rango establecido: ", rango)

    if numero > rangoI and numero > rangoF:
        print("El numero ingresado No esta en el rango establecido: ", rango)

    return rango

rangoI = int(input("Ingrese el rango inicial: "))
rangoF = int(input("Ingrese el rango final: "))
numero = int(input("Ingrese el numero: ")) 

if rangoF > rangoI:
    rango = Rango_Determinado(numero, rangoI, rangoF)
else:
    print("El rango Inicial no debe ser mayor que el rango final")







