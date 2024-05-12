#Funciones comprobar si la cadena es palindromo o no

def palindromo(frase):
    Texto = frase.lower().replace(" ", "") #convertir en minusculas y quitar espacios
    Frase_Invertida = ''.join(reversed(Texto)) # invocamos la funcion join para una cadena de caracteres y la funcion reversed
    return Texto == Frase_Invertida

Texto = input("Ingrese la Frase palindroma: ")

if  palindromo(Texto):
       print("La Frase que ha escrito es Palindroma")
else:
       print("La Frase que ha escrito no es Palindroma")

