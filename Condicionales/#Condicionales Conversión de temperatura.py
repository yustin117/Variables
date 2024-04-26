#Condicionales Conversión de temperaturas. Crear un menú de opciones. 
Conver = """
1 Fahrenheit -> Celsius
2 Fahrenheit -> Kelvin
3 Fahrenheit -> Rankine
4 Fahrenheit -> Reaumur
5 Celsius -> Fahrenheit
6 Celsius -> Kelvin
7 Celsius -> Rankine
8 Celsius -> Reaumur
9 Kelvin -> Fahrenheit
10 Kelvin -> Celsius
11 Kelvin -> Rankine
12 Kelvin -> Reaumur
13 Rankine -> Fahrenheit
14 Rankine -> Celsius
15 Rankine -> Kelvin
16 Rankine -> Reaumur
17 Reaumur -> Fahrenheit
18 Reaumur -> Celsius
19 Reaumur -> Kelvin
20 Reaumur -> Rankine
"""
Conver = int(input("Seleccionar la conversion de temperatura: "))
Temp = float(input("Digitar la temperatura de conversion: "))
if Conver == 1:
    Formula = (Temp-32)/1.8
    print("La conversion de la temperatura es: ",round(Formula,1),)
    print("Celsius")
elif Conver == 2:
    Formula = (Temp+459.67)/1.8
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Kelvin")
elif Conver == 3:
    Formula = (Temp+459.67)
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Rankine")
elif Conver == 4:
    Formula = (Temp-32)/2.25
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Reaumur")
elif Conver == 5:
    Formula = (Temp*1.8)+32
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Fahrenheit")
elif Conver == 6:
    Formula = (Temp+273.15)
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Kelvin")
elif Conver == 7:
    Formula = (Temp*1.8)+32+459.67
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Rankine")
elif Conver == 8:
    Formula = (Temp*0.8)
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Reaumur")
elif Conver == 9:
    Formula = (Temp*1.8)-159.67
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Fahrenheit")
elif Conver == 10:
    Formula = (Temp-273.15)
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Celsius")
elif Conver == 11:
    Formula = (Temp*1.8)
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Rankine")
elif Conver == 12:
    Formula = (Temp-273.15)*0.8
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Reaumur")
elif Conver == 13:
    Formula = (Temp-459.67)
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Fahrenheit")
elif Conver == 14:
    Formula = (Temp-32)/1.8
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Celsius")
elif Conver == 15:
    Formula = (Temp/1.8)
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Kelvin")
elif Conver == 16:
    Formula = (Temp-32)/2.25
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Reaumur")
elif Conver == 17:
    Formula = (Temp*2.25)+32
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Fahrenheit")
elif Conver == 18:
    Formula = (Temp*1.25)
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Celsius")
elif Conver == 19:
    Formula = (Temp*1.25)+273.15
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Kelvin")
elif Conver == 20:
    Formula = (Temp*2.25)+32+459.67
    print("La conversion de la temperatura es: ",round(Formula,1))
    print("Rankine")
else:
    print("Convercion no Disponible")


