ftotal = float(input('Introdueix el preu de tot el carrito: '))

def amb_iva(ftotal, iva):
    ftotal = ftotal * iva   
    return ftotal

print(amb_iva(ftotal,21))