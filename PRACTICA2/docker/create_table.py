import psycopg2

def create_users_table(cursor):
    try:
        sql_query = '''CREATE TABLE IF NOT EXISTS USERS(
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(255) NOT NULL,
                        user_surname VARCHAR(255) NOT NULL,
                        user_age BIGINT NOT NULL,
                        user_email VARCHAR(255) NOT NULL)'''
                        
        cursor.execute(sql_query)
        cursor.connection.commit()  # Utilitza la connexió del cursor per fer el commit
        print("Taula USERS creada correctament.")
    except (Exception, psycopg2.Error) as error:
        print("Error en crear la taula USERS:", error)
