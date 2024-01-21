def mostra_numeros(numero1, numero2):
    suma = 0
    for i in range(numero1+1, numero2):
        suma += i
        print(i)

    print(f'Suma total: {suma}')