#Condicionales Notas: aprobo o no aprobo
Not1 = float(input("Ingresa la nota 1: "))
Not2 = float(input("Ingresa la nota 2: "))
Not3 = float(input("Ingresa la nota 3: "))
Not4 = float(input("Ingresa la nota 4: "))
Not5 = float(input("Ingresa la nota 5: "))
promedio = (Not1+Not2+Not3+Not4+Not5)/5
print("El promedio de las 5 notas es: ",round(promedio,1))
if promedio >= 3.0:
    print("El estudiante aprobo el semestre")
else:
    print("El estudiante no aprobo el semestre")

    
    
