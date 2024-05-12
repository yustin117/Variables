#Funciones invertir una cadena

def Frase ():
    invertir = input("Escriba la frase que desea: ")
    Frase_Invertida = ''.join(reversed(invertir))
    return Frase_Invertida

Resultado = Frase()
print("Así queda la inversion de la frase escrita: ", Resultado)



