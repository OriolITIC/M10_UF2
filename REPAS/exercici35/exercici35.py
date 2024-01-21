def analitzar_frase(frase):
    paraules = frase.split()
    longitud_paraules = {paraula: len(paraula) for paraula in paraules}
    return longitud_paraules