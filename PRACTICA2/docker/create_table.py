import psycopg2

#####################  CREATE TABLE  ###########################

def create_users_table(mydb,cursor):
    try:
        # Query a executar: Crear una taula si no existeix
        sql_query = '''CREATE TABLE IF NOT EXISTS USERS(
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(255) NOT NULL,
                        user_surname VARCHAR(255) NOT NULL,
                        user_age BIGINT NOT NULL,
                        user_email VARCHAR(255) NOT NULL)'''
        
        # Executar la consulta SQL               
        cursor.execute(sql_query)
        
        # Realitzar commit per a confirmar els canvis a la base de dades
        mydb.commit()  
        print("Taula USERS creada correctament.")
    except (Exception, psycopg2.Error) as error:
        print("Error en crear la taula USERS:", error)
        
###############################################################
