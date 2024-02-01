import connection

def update_user(self,connection):
        try:
            sql_update = ''' UPDATE public.users SET user_email='oriol@email.com' WHERE user_id=1'''
           
            connection.execute(sql_update)
           
        except Exception as error:
            print("Error al actualizar el usuari:", error)