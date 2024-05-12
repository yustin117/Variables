#Funciones contador de Minusculas y Mayusculas

def letras_Mayusculas_Minusculas(Texto):
    contador = {"Minusculas": 0, "Mayusculas": 0}

    for i in Texto:
        if i.isupper():
            contador ["Mayusculas"] += 1
        elif i.islower():
            contador ["Minusculas"] += 1
    return contador

Frase = input("Escriba la frase que desea: ")
print (letras_Mayusculas_Minusculas(Frase))

     
