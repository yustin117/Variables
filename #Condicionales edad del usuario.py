#Condicionales edad del usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad:"))
if edad >= 100:
    print("Ingrese una edad valida")
elif edad <= -1:
    print("Ingrese una edad valida")
elif edad >= 18:
    print("Eres mayor de edad")
elif edad < 18:
    print("Eres menor de edad")