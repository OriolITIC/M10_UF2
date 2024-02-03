import psycopg2

########################  DELETE  ##############################

def delete_user(mydb,cursor):
    try:
        # Query a executar: Eliminar el usuari amb user_id = 1
        sql_delete = '''DELETE FROM public.USERS WHERE user_id = 1'''
        
        # Executar la consulta SQL
        cursor.execute(sql_delete)
        
        # Realitzar commit per a confirmar els canvis a la base de dades
        mydb.commit()
        
        print("Usuari eliminat correctament.")
    except (Exception, psycopg2.Error) as error:
        print("Error en eliminar l'usuari:", error)

###############################################################