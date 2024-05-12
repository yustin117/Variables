#Funciones El maximo de tres numeros

def numeros (num1,num2,num3):
    if num1>num2>num3:
        print(f"El numero mayor es: {num1}")
        print(f"El numero del medio es : {num2}")
        print(f"El numero menor es: {num3}")
    elif num2>num1>num3:
        print(f"El numero mayor es: {num2}")
        print(f"El numero del medio es : {num1}")
        print(f"El numero menor es: {num3}")
    elif num3>num2>num1:
        print(f"El numero mayor es: {num3}")
        print(f"El numero del medio es : {num2}")
        print(f"El numero menor es: {num1}")
    elif num1>num3>num2:
        print(f"El numero mayor es: {num1}")
        print(f"El numero del medio es : {num3}")
        print(f"El numero menor es: {num2}")
    elif num2>num3>num1:
        print(f"El numero mayor es: {num2}")
        print(f"El numero del medio es : {num3}")
        print(f"El numero menor es: {num1}")
    elif num3>num1>num2:
        print(f"El numero mayor es: {num3}")
        print(f"El numero del medio es : {num1}")
        print(f"El numero menor es: {num2}")
    else:
        print("Hay numeros repetidos") 

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el Tercer numero: "))

variable = numeros (num1,num2,num3)
print(variable)