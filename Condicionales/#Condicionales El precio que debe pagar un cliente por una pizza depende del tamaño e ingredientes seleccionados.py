#Condicionales El precio que debe pagar un cliente por una pizza depende del tamaño y e ingrediente seleccionado:
print('''
Bienvenido al programa de pago de pizza
Los tamaños a seleccionar son 3: 
1 -> 15000
2 -> 24000
3 -> 36000 

Cada Adición tiene un valor de 4000     
''')

tamaño_pizza = int(input("Ingrese el tamaño de la pizza elejida por el cliente:"))
ingredientes = int(input("Ingrese la cantidad de ingredientes adicionales solicitadas por el cliente:"))

valor_ingredientes = 4000*ingredientes

if tamaño_pizza == 1 : 
    valor_pizza = 15000
    total_pagar = valor_pizza + valor_ingredientes
    print("El tamaño de la pizza tiene un costo de:", valor_pizza)
    print("Los ingredientes seleccionados tienen un costo de:", valor_ingredientes)
    print("El valor a pagar es de:", total_pagar)
elif tamaño_pizza == 2 :
    valor_pizza = 24000
    total_pagar = valor_pizza + valor_ingredientes
    print("El tamaño de la pizza tiene un costo de:", valor_pizza)
    print("Los ingredientes seleccionados tienen un costo de:", valor_ingredientes)
    print("El valor a pagar es de:", total_pagar)
elif tamaño_pizza == 3 : 
    valor_pizza = 36000
    total_pagar = valor_pizza + valor_ingredientes
    print("El tamaño de la pizza tiene un costo de:", valor_pizza)
    print("Los ingredientes seleccionados tienen un costo de:", valor_ingredientes)
    print("El valor a pagar es de:", total_pagar)
else:
    print("Tamaño de pizza no encontrado")






