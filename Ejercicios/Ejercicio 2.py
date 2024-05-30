#Enumerando lineas, palabras, caracteres de un texto

import sys

stdout_original = sys.stdout
print(
'''
Bienvenido al programa de acciones sobre un archivo de texto Plano 
Tener en cuenta los siguientes aspectos 
1. Cuando se solicite colocar la ruta y nombre de archivo debes colocarlo como en el siguiente ejemplo: 
    C:/holamundo.txt
''')

nombre_archivo_salida = "informacion_resultados.txt"
ruta = input("Por favor, indique la ruta y el nombre del archivo: ")
#ruta = r"C:\Users\yusti\OneDrive\Documentos\Parrafo.txt"

try:
    with open(nombre_archivo_salida, 'w') as archivo_salida:
        sys.stdout = archivo_salida

        print(
'''
Bienvenido al programa de acciones sobre un archivo de texto Plano 
Tener en cuenta los siguientes aspectos 
1. Cuando se solicite colocar la ruta y nombre de archivo debes colocarlo como en el siguiente ejemplo: 
    C:/holamundo.txt
''')

        simbolos = ['¿','?','.',',',';',':','¡','!']
        palabrotas = 0
        frecuencia = {}

        with open(ruta, 'r', encoding='utf-8') as fichero:
            conteo_lineas = len(fichero.readlines())
            print("RESPUESTA PUNTO 1")
            print("---------------------------------------------")
            print("la cantidad de lineas son:", conteo_lineas)
            print("---------------------------------------------")
            fichero.seek(0)

            for linea in fichero: 
                for x in simbolos: 
                    linea = linea.replace(x,'')
                palabras = linea.split()
                palabrotas += len(palabras)
                for una_palabra in palabras:
                    una_palabra = una_palabra.lower()
                    if una_palabra in frecuencia: 
                        frecuencia[una_palabra] += 1
                    else:
                        frecuencia[una_palabra] = 1
            print("RESPUESTA PUNTO 2")
            print("---------------------------------------------")
            print("La cantidad de palabras son:", palabrotas)
            print("---------------------------------------------")
            fichero.seek(0)
            cuenta_caracteres = len(fichero.read())
            print("RESPUESTA PUNTO 3")
            print("---------------------------------------------")
            print("La cantidad de caracteres son:", cuenta_caracteres)
            print("---------------------------------------------")

        print("RESPUESTA PUNTO 4")
        print("---------------------------------------------")
        for la_palabra_final in frecuencia:
            plural_singular = 'veces'
            if frecuencia[la_palabra_final] == 1:
                plural_singular = 'vez'
            print('La palabra "%s" se ha repetido %s %s' %(la_palabra_final, frecuencia[la_palabra_final], plural_singular))
        print("---------------------------------------------")

finally:
    sys.stdout = stdout_original