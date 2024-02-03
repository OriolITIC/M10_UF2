import psycopg2

##########################  UPDATE ############################

def update_user(mydb,cursor):
    try:
        # Query a executar: Actualitzar el correu electrònic del usuari amb user_id = 1
        sql_update = ''' UPDATE public.USERS SET user_email='ori@outlook.com' WHERE user_id=3 '''
        
        # Executar la consulta SQL
        cursor.execute(sql_update)
        
        # Realitzar commit per a confirmar els canvis a la base de dades
        mydb.commit()
        
        # Obtindre el nombre de files modificades
        result = cursor.rowcount

        print("id modificada: ", result, "Actualització efectuada sense errors ")
    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar el usuario:", error)
        
###############################################################