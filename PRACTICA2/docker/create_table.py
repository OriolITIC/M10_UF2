import connection

def create_users_table(self,connection):
    try:
        sql_query = '''CREATE TABLE IF NOT EXISTS USERS(
                        user_id SERIAL PRIMARY KEY,
                        user_name VARCHAR(255) NOT NULL,
                        user_surname VARCHAR(255) NOT NULL,
                        user_age BIGINT NOT NULL,
                        user_email VARCHAR(255) NOT NULL
                        )'''
                        
        self.cursor.execute(sql_query)
        connection.commit()
        print("Tabla USERS creada correctamente.")
    except Exception as error:
        print("Error al crear la tabla USERS:", error)