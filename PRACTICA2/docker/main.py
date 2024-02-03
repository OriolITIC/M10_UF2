import connection
import create_table
import create
import delete
import read
import update

if __name__ == "__main__":
    try:
        # Intenta establir la conexió amb la base de dades
        mydb, cursor = connection.establir_connexio()

        if mydb:
            while True:
                print("\n============== MENU ===================")
                print("Elegeix una opció:\n ")
                print("(a) Crear taula usuaris")
                print("(b) Inserir un nou usuari")
                print("(c) Llegir tots els usuaris")
                print("(d) Modificar els camps d'un usuari")
                print("(e) Eliminar un usuari")
                print("(f) Sortir")
                print("\n")

                opcio = input()             

                # Realitza l'operació segons l'opció seleccionada
                match opcio:
                    case 'a':
                        create_table.create_users_table(mydb, cursor)
                    case 'b':
                        create.insert_user(mydb, cursor)
                    case 'c':
                        read.get_users(cursor)
                    case 'd':
                        update.update_user(mydb, cursor)
                    case 'e':
                        delete.delete_user(mydb, cursor)
                    case 'f':
                        break  # Surt del bucle i finalitza l'aplicatiu
                    case _:
                        print("Opció no vàlida. Torna a intentar.")
                    
    except Exception as e:
        # Si no es pot establir la connexió amb la base de dades, imprimeix un missatge d'error
        print("S'ha produït un error en interactuar amb la base de dades:", e)
    
    finally:
        # Tanca la connexió a amb la base de dades
        if mydb:
            connection.tancar_connexio(mydb)
            print('Connexió tancada correctament') 

