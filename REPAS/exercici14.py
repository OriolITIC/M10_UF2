numeros = input("Introdueix deu numeros separats per espai: ")
numeros_llista = numeros.split()
tupla_numeros = tuple()

for numero in numeros_llista:
    tupla_numeros += (int(numero),)  

print("La tupla de números és:", tupla_numeros)
print(type(tupla_numeros))