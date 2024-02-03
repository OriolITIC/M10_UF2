import psycopg2

def insert_user(cursor):
    try:
        sql_query = ''' INSERT INTO public.USERS(user_id, user_name, user_surname, user_age, user_email)
                        VALUES ('1', 'Oriol', 'Martinez', '32', 'oriol.martinez@gmail.com') '''
        cursor.execute(sql_query)  
        print("Usuari insertat correctament.")
        cursor.connection.commit()  
    except (Exception, psycopg2.Error) as error:
        print("Error en insertar l'usuari:", error)