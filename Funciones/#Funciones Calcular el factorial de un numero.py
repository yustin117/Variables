#Funciones Calcular el factorial de un numero

def Factorial(n):
    if n < 0:
        return "No se acepta numeros negativos"
    if n == 0 or n == 1:
        return 1
    for i in range (1,n):
        n = n*i
    return n

Numero = Factorial (int(input("Ingrese el valor que quiere calcular: ")))
print("La factorial del numero ingresado es: ", Numero)

    
 



