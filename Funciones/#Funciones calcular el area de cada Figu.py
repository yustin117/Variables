#Funciones Calcular el area de cada Figura 

def Rectangulo(a,b):
    return a*b 

def Cuadrado(a):
    return a*a

def Paralelograma(a,b):
     return a*b 

def Rombo(a,b):
    return a*b/2 

def Trapecio(a,b,c):
    return (a+b/2)*c

def Triangulo(a,b):
    return a*b/2 

def Triangulo_Equilatero(a):
    return a*a*3**0.5/4 

def Triangulo_Rectangulo(a,b):
    return a*a/2

def Poligono_Regular(a,b):
    return b*a/2

print('''
 Rectangulo -> 1
 Cuadrado -> 2
 Paralelograma -> 3
 Rombo -> 4
 Trapecio -> 5
 Triangulo -> 6
 Triangulo_Equilatero -> 7
 Triangulo_Rectangulo -> 8
 Poligono_Regular -> 9
''')

Figura_Geometrica = int(input("Seleccione el numero de la figura geométrica a calcular: "))

if Figura_Geometrica == 1:
    a = int(input("cual es lado del rectangulo: "))
    b = int(input("cual es el otro lado: "))
    print("El área del rectangulo es:", Rectangulo(a,b))

if Figura_Geometrica == 2:
    a = int(input("Cual es el lado del Cuadrado: "))
    print("El área del Circulo es:", Cuadrado(a))

if Figura_Geometrica == 3:
    a = int(input("cual es la base del paralelograma: "))
    b = int(input("cual es la altura del paralelograma: "))
    print("El área del Paralelograma es:", Paralelograma(a,b))

if Figura_Geometrica == 4:
    a = int(input("cual es la longitud de la diagonal mayor del Rombo: "))
    b = int(input("cual es la longitud de la diagonal menor del Rombo: "))
    print("El área del Rombo es:", Rombo(a,b))

if Figura_Geometrica == 5:
    a = int(input("cual es el lado paralelo del trapecio: "))
    b = int(input("cual es el otro lado paralelo del trapecio: "))
    c = int(input("cual la distancia perpendicular entre los lados paralelos: "))
    print("El área del Trapecio es:", Trapecio(a,b,c))

if Figura_Geometrica == 6:
    a = int(input("cual es la base del triangulo: "))
    b = int(input("cual es la altura del triangulo: "))
    print("El área del Triangulo es:", Triangulo(a,b))

if Figura_Geometrica == 7:
    a = int(input("cuales son los lados del Triangulo Equilatero: "))
    print("El área del Triangulo Equilatero es:", Triangulo_Equilatero(a)) 

if Figura_Geometrica == 8:
    a = int(input("cual es el cateto opuesto del Traiangulo Rectangulo: "))
    b = int(input("cual es el cateto adyacente del Triangulo Rectangulo: "))
    print("El área del Triangulo Rectangulo es:", Triangulo_Rectangulo(a,b))

if Figura_Geometrica == 9:
    a = int(input("cual es el perimetro del Poligono Regular: "))
    b = int(input("cual es el apotema del Poligono Rgular: "))
    print("El área del Poligono_Regular es:", Poligono_Regular(a,b))









    









