#Funciones identificar si el numero es primo o no

def numero_primos(n):
    a = 1
    b = 0
    while a <= n:
        if n % a == 0:
            b = b + 1
        a = a + 1
    if b == 2:
        print("El numero que ha ingresado es primo: ")
    else:
        print("El numero que ha ingresado no es primo: ")
    return n

Numero = int(input("Registe el numero a identificar: "))
print (numero_primos(Numero))

