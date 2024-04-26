#Condicionales Solicitar número al usuario y determinar si es par, impar o es cero. 
num1 = int(input("Digite numero: "))
if num1 == 0:
    print("El numero es cero")
elif num1%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")