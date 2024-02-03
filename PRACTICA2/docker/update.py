import psycopg2

def update_user(cursor):
    try:
        sql_update = ''' UPDATE public.USERS SET user_email='oriol@outlook.com' WHERE user_id=1'''
        cursor.execute(sql_update)
        cursor.connection.commit()
        result = cursor.rowcount
        print("id modificada: ", result, "Actualització efectuada sense errors ")
    except (Exception, psycopg2.Error) as error:
        print("Error al actualizar el usuario:", error)