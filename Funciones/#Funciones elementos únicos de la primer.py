#Funciones elementos únicos de la primera lista

def Listas_numeros(numeros):
    return list(set(numeros))

Lista = [1,2,2,3,4,5,5,5,6,7,8,8,9,9,10]
valores_unicos = Listas_numeros(Lista)

print("lista original de numeros: ", Lista)
print("Lista actualizada de numeros: ", valores_unicos)


