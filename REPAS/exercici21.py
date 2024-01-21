numeros = input("Introdueix 10 numeros separats per espais: ")
numeros = numeros.split()
print(numeros)

suma = 0

for numero in numeros:
    suma = suma + int(numero)

mitjana = suma/len(numeros)

print(f'Numeros de lusuari: {numeros}')
print(f'Suma total: {suma}')
print(f'Mitjana: {mitjana}')