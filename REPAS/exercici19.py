areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa",
             15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació", 12.23]

print(areas_pis[1])
print(areas_pis[-1])
print(areas_pis[7])
print(areas_pis[:3])
print(areas_pis[3:])
print(areas_pis[5]+areas_pis[13])

areas_pis[9] = 8.12
print(areas_pis)
areas_pis.append("pati interior")
areas_pis.append(2.78)


for i in range(1, len(areas_pis), 2):
    print(areas_pis[i])
