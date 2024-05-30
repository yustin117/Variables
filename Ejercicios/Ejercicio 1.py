#Contraseñas seguras

import random

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}*,.;:/-+=_!¡¿?'$<>#$&"

caracteres = minus+mayus+numeros+simbolos
longitud = 12

muestra = random.sample(caracteres, longitud)
print(muestra)
contraseña = "".join(muestra)
print (contraseña)
print("Esta es la contraseña que se ha establecido: ", contraseña)

fichero = open("Contraseña.txt","w")
fichero.write(contraseña)
fichero.close()



