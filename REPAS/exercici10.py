import random

numero_a_endivinar = random.randint(1, 100)

intents = 0
endivinat = False

while not endivinat:
    intent = int(input("Introdueix el teu numero: "))
    intents += 1

    if intent == numero_a_endivinar:
        print(f"¡Has endivinat el número {numero_a_endivinar} en {intents} intentos!")
        adivinado = True
    elif intent < numero_a_endivinar:
        print("El número es major. ¡Segueix intentant!")
    else:
        print("El número es menor. ¡Segueix intentant!")
