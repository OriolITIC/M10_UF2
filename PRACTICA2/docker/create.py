import psycopg2

########################  CREATE  #############################

def insert_user(mydb,cursor):
    try:
        # Query a executar: Insertar un nou usuari amb les dades especificades
        sql_query = ''' INSERT INTO public.USERS(user_id, user_name, user_surname, user_age, user_email)
                        VALUES ('3', 'Oriol', 'Martinez', '32', 'oriolmmm.martinez@gmail.com') '''
        
        # Executar la consulta SQL
        cursor.execute(sql_query)  
        
        # Realitzar commit per a confirmar els canvis a la base de dades
        mydb.commit()  

        print("Usuari inserit correctament.")
    except (Exception, psycopg2.Error) as error:
        print("Error a l'inserir l'usuari:", error)
        
###############################################################





