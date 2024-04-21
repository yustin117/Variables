#Variables Calcular precio con IVA
print("Cantidad de productos:")
print("Nombre del producto:")
prods = int(input())
i=0
sub=0
while i<prods:
    print("producto, valor:")
    val = int(input())
    print("Cantidad") 
    cant = int(input())
    subpro=val*cant
    sub=sub+subpro
    i+=1
    iva = sub * 0.16
    total = sub + iva
print("Vendieron: ",prods," productos")
print("Subtotal: ",sub)
print("IVA 16% ",iva)
print("Total: ", total)