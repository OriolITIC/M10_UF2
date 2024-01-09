paraules = input("Introdueix 2 paraules separedes per espai:")

paraules_llista = paraules.split()
par1 = paraules_llista[0][0] + paraules_llista[0][1]
par2 = paraules_llista[1][0] + paraules_llista[1][1]
print(par2 + paraules_llista[0][2:] + " " + par1 + paraules_llista[1][2:])