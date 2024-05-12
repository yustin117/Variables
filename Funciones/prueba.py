def Rectangulo(a,b):
    return a*b 

print('''
    1. Rectangulo
''')

figura = int(input("Seleccione el numero de la figura geométrica a calcular:"))

if figura == 1:
    a = int(input("cual es lado del rectangulo: "))
    b = int(input("cual es el otro lado: "))
    print("El área del rectangulo es:", Rectangulo(a,b))
