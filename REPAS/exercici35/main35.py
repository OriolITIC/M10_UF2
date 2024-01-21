import exercici35

frase = input("Introdueix una frase: ")
resultat = exercici35.analitzar_frase(frase)

for paraula, longitud in resultat.items():
    print(f"Paraula: {paraula} - longitud: {longitud}")