#Condicionales menu de calculo de figuras geometricas
FigurasGeo = """
1 Rectangulo
2 Cuadrado
3 Paralelogramo
4 Rombo
5 Trapecio
6 Triangulo
7 Triangulo equilatero
8 Triangulo rectangulo
9 Poligono regular
"""
FigurasGeo = int(input("Seleccionar la figura geometrica: "))

if FigurasGeo == 1:
    a = int(input("Digite el valor del primer lado: "))
    b = int(input("Digite el valor del segundo lado: "))
    Area1 = a*b
    print("El area del Rectangulo es: ",round(Area1,1))
elif FigurasGeo == 2:
    a = int(input("Digitar numero: "))
    Area2 = a*a
    print("El area del Cuadrado es: ",round(Area2,1))
elif FigurasGeo == 3:
    a = int(input("Digitar numero: "))
    b = int(input("Digitar numero: "))
    Area3 = a*b
    print("El area del Paralelograma es: ",round(Area3,1))
elif FigurasGeo == 4:
    a = int(input("Digitar numero: "))
    b = int(input("Digitar numero: "))
    Area4 = a*b/2
    print("El area del Rombo es: ",round(Area4,1))
elif FigurasGeo == 5:
    a = int(input("Digitar numero: "))
    b = int(input("Digitar numero: "))
    c = int(input("Digitae numero "))
    Area5 = (a+b/2)*c
    print("El area del Trapecio es: ",round(Area5,1))
elif FigurasGeo == 6:
    a = int(input("Digitar numero: "))
    b = int(input("Digitar numero: "))
    Area6 = a*b/2
    print("El area del Triangulo es: ",round(Area6,1))
elif FigurasGeo == 7:
    a = int(input("Digitar numero: "))
    Area7 = a*a*3**0.5/4
    print("El area del Triangulo equilatero es: ",round(Area7,1))
elif FigurasGeo == 8:
    a = int(input("Digitar numero: "))
    Area8 = a*a/2
    print("El area del Triangulo rectangulo es: ",round(Area8,1))
elif FigurasGeo == 9:
    a = int(input("Digitar numero: "))
    b = int(input("Digitar numero: "))
    Area9 = b*a/2
    print("El area del Poligono regular es: ",round(Area9,1))
else:
    print("Figura no existente")
