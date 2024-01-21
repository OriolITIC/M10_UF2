contactes = {'Roger': 678232311, 'Oriol': 566879326}

def elimina(contactes, user):
    if user in contactes:
        del contactes[user]
        print(f"S'ha eliminat l'usuari {user} de la llista de contactes.")
        return contactes
    else:
        return f"L'usuari {user} no existeix a la llista de contactes."
    
elimina(contactes, 'Roger')
print(contactes)
