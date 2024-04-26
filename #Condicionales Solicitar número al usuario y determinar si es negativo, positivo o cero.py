#Condicionales Solicitar número al usuario y determinar si es negativo, positivo o cero.
num1 = int(input("Digite numero: "))
if num1 == 0:
    print("El numero es cero")
elif num1 <= -1:
    print("El numero es negativo")
else:
    print("El numero es positivo")