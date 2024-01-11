numero = int(input("Introdueix un numero entr 1 i 100: "))

if numero in range(1,100):

    numeros = tuple(range(1, numero + 1))
    print("La tupla amb els numeros es:", numeros)
else:
    print("Numero fora del rang")
