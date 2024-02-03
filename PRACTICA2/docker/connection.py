import psycopg2

# Establece la connexió amb la base de dades
def establir_connexio():
    try:
        mydb = psycopg2.connect(
            database="postgres",
            user="user_postgres",
            password="pass_postgres",
            host="localhost",
            port="5432"
        )
        
        print('Connexió establerta correctament')
        return mydb, mydb.cursor()
        
    except psycopg2.Error as e:
        print("Error al connectar a la base de dades:", e)

def tancar_connexio(mydb):
    mydb.close()

