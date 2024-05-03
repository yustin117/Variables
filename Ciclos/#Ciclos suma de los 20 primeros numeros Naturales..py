#Ciclos suma de los 20 primeros numeros Naturales.
numN = int(input())
print("Digitar el numero natural: ", numN)
suma = 0
for N in range (1, numN+1):
    print(N)
    suma = suma + N
print ("El total de la suma de los 20 numeros naturales es: ", suma)
