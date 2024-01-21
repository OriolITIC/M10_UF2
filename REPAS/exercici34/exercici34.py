def calcular_quadrat(numero):
    return numero ** 2

def calcular_quadrats(llista_numeros):
    llista_quadrats = []

    for numero in llista_numeros:
        llista_quadrats.append(calcular_quadrat(numero))
    return llista_quadrats