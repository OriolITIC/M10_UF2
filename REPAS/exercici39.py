n = int(input("Introdueix l’alçada del triangle (enter positiu): "))

for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")