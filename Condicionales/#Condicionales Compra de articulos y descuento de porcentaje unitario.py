#Condicionales Compra de articulos y descuento de porcentaje unitario
print("Bienvenido a la tienda de todo a 5000")

porcentaje = 0.05
porcentaje2 = 0.08
Articulo = int(input("Ingrese la cantidad de articulos que quiere comprar: "))
valor_punitario = int(input("Ingrese el valor del precio unitario:"))

if Articulo <= 5:
    valor_total = Articulo*valor_punitario
    print("El total de pagar por lo comprado es de: ", valor_total)
elif Articulo > 5 and Articulo < 10:
    descuento = valor_punitario*porcentaje
    valor_total = Articulo*(valor_punitario-descuento)
    print("El total de pagar por lo comprado es de: ", valor_total)
else:
    descuento = valor_punitario*porcentaje2
    valor_total = Articulo*(valor_punitario-descuento)
    print("El total de pagar por lo comprado es de: ",valor_total)

    








