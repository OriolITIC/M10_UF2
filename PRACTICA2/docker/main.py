import connection
import create_table
import create
import delete
import read
import update

if __name__ == "__main__":
    try:
        cursor = connection.establir_connexio()  # Establim la connexió a la base de dades

        if cursor:
            try:
                create_table.create_users_table(cursor)
                #create.insert_user(cursor)  
                #delete.delete_user(cursor)
                read.get_users(cursor)
                update.update_user(cursor)
               
            except Exception as e:
                print("S'ha produït un error en interactuar amb la base de dades:", e)
            finally:
                cursor.close()  
        else:
            print("No s'ha pogut establir la connexió.")
    except Exception as e:
        print("S'ha produït un error en establir la connexió:", e)

