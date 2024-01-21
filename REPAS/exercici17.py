frase = input("Introdueix una frase: ")
frase_list = frase.split(' ')
frase_tuple = tuple()

for paraula in frase_list:
    paraula = ''.join(list(set(paraula)))
    frase_tuple += (paraula,)
    
print(frase_tuple)

