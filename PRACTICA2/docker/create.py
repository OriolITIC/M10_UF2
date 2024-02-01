import psycopg2
import connection

def insert_user(self):
    try:
        cursor = connection.cursor()
        sql_query = ''' INSERT INTO public.users(user_id, user_name, user_surname, user_age, user_email)
                        VALUES ('1', 'Oriol', 'Martinez', '32', 'oriol.martinez@gmail.com') '''
        connection.execute(sql_query)
        print("Usuario insertado correctamente.")
    except (Exception, psycopg2.Error) as error:
        print("Error al insertar el usuario:", error)
    finally:
        if cursor:
            cursor.close()

def close_connection(self):
    connection.close_connection() 



