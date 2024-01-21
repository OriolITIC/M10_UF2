numero = int(input("Introdueix un numero: "))

tupla_numeros = tuple()
while(numero != 0):
    tupla_numeros += (int(numero),)  
    numero = int(input("Introdueix un numero: "))

tupla_sorted = tuple(sorted(tupla_numeros))

print("La tupla de números és:", tupla_sorted)
print(type(tupla_sorted))