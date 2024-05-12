def en_rango(numero, rangoinicial, rangofinal):
    return numero >= rangoinicial and numero <= rangofinal

numero = int(input("ingrese numero:"))

rangoinicial = int(input("ingrese numero:"))

rangofinal = int(input("ingrese numero:"))

if en_rango(numero, rangoinicial, rangofinal): 
    print ("El numero se encuentra dentro del rango")
else:
    print("El numero no se encuentra dentro del rango")