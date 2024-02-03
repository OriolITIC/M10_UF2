import psycopg2
      
###########################  READ  ############################

def get_users(cursor):
    try:
        # Query a executar: Obtindre tots els usuaris de la taula
        sql_get = ''' SELECT user_id,user_name, user_surname, user_age, user_email
                      FROM public.users'''
        
        # Executar la consulta SQL
        cursor.execute(sql_get)
        
        # Obtindre tots els resultats de la consulta
        result = cursor.fetchall()
        
        # Imprimir les dades de cada usuari
        for i in result:
            print("user_id: ", i[0])
            print("user_name: ", i[1])
            print("user_surname: ", i[2])
            print("user_age: ", i[3])
            print("user_email: ", i[4], "\n")
    except (Exception, psycopg2.Error) as error:
        print("Error al obtener los usuarios:", error)

###############################################################