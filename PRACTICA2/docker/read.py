import psycopg2

def get_users(cursor):
    try:
        sql_get = ''' SELECT user_id,user_name, user_surname, user_age, user_email
                    FROM public.users'''
        cursor.execute(sql_get)
        
        result = cursor.fetchall()
        
        for i in result:
            print("user_id: ", i[0])
            print("user_name: ", i[1])
            print("user_surname: ", i[2])
            print("user_age: ", i[3])
            print("user_email: ", i[4], "\n")
    except (Exception, psycopg2.Error) as error:
        print("Error al obtener los usuarios:", error)
