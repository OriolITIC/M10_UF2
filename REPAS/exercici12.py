mesos = ('Gener','Febrer','Març','Abril','Maig','Juny','Juliol','Agost','Septembre','Octubre','Novembre','Desembre')
numero = int(input("Introdueix un numero entre 1 i 100: "))

while(numero != 0):
    print(mesos[numero-1])
    numero = int(input("Introdueix un numero entre 1 i 100: "))