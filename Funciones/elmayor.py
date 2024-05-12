#Funciones El maximo de tres numeros

def el_mayor (num1,num2,num3):
    mayor = num1

    if num2 > mayor: 
        mayor=num2
    
    if num3 > mayor: 
        mayor=num3 

    return mayor

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el Tercer numero: "))

mayor = el_mayor(num1,num2,num3)

print ("El numero mayor es:", mayor)