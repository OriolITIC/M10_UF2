valor1 = int(input("Introdueix un valor:"))
valor2 = int(input("Introdueix un valor:"))

if valor1 > valor2:
    print(f'{valor1} es mes gran')
elif valor1 < valor2:
    print(f'{valor2} es mes gran')
else:
    print(f'Els valors son iguals')