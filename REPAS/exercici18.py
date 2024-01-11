paraules = input("Introdueix 2 paraules: ")

paraules = paraules.split()
print(paraules)

for paraula in paraules:
    lletres_repetides = []
    for lletra in paraula:
        if(lletra not in lletres_repetides):
            num_lletra = paraula.count(lletra)
            print(lletra + ": " +str(num_lletra))
            lletres_repetides.append(lletra)