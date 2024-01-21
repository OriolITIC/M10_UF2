dic = {}

nom = input("Introduce el nom de la persona: ")

while nom != "":
    
    if nom in dic:
        print("El nom ja està al diccionari")
        continue

    edat = int(input("Introdueix la edat de la persona: "))
    dic[nom] = edat
    nom = input("Introduce el nom de la persona: ")

print(f'Llista de persones final: {dic}')
