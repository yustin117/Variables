n = int(input("Ingrese el número de términos de la serie de Fibonacci que desea mostrar: "))

# Inicializar un vector para almacenar los términos de la serie
fibonacci = [0, 1]

# Calcular los términos de la serie y almacenarlos en el vector
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

# Calcular la suma de los términos
suma = sum(fibonacci)

# Mostrar los términos y la suma
print("Los primeros", n, "términos de la serie de Fibonacci son:")
print(*fibonacci, sep=", ")
print("La suma de los primeros", n, "términos de la serie de Fibonacci es:", suma)