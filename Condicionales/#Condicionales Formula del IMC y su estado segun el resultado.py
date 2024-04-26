#Condicionales Formula del IMC y su estado segun el resultado
print("Claculadora del IMC")
P = float(input("Digite su peso en Kilogramos por favor: "))
E = float(input("Digite su estatura en Metros por favor: "))
IMC = P/(E*E)
if IMC < 18.5:
    Estado = IMC
    print("Segun los resultados del IMC se encuentra en un estado Desnutrido: ", round(Estado,1))
elif IMC >= 18.5 and IMC <= 24.9:
    Estado2 = IMC
    print("Segun los resultados del IMC se encuentra en un estado Normal: ", round(Estado2,1))
elif IMC >= 25 and IMC <= 29.9:
    Estado3 = IMC
    print("Segun los resultados del IMC se encuentra en un estado de Sobrepeso: ", round(Estado3,1))
elif IMC >= 30 and IMC <= 34.9:
    Estado4 = IMC
    print("Segun los resultados del IMC se encuentra en un estado de Obecidad Grado 1 : ", round(Estado4,1))
elif IMC >= 35 and IMC <= 39.9:
    Estado5 = IMC
    print("Segun los resultados del IMC se encuentra en un estado de Obecidad Grado 2: ", round(Estado5,1))
elif IMC >= 40 and IMC <= 49.9:
    Estado6 = IMC
    print("Segun los resultados del IMC se encuentra en un estado de Obecidad Grado 3: ", round(Estado6,1))
else:
    IMC <= 50
    Estado7 = IMC
    print("Segun los resultados del IMC se encuentra en un estado de Obecidad Grado 4: ", round(Estado7,1))
