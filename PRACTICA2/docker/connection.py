import psycopg2

# Per saber quina és la database, el user i el password mirar el .yml
def establir_connexio():
    mydb = psycopg2.connect(
    database="postgres",
    user="user_postgres",
    password="pass_postgres",
    host="localhost",
    port="5432")

    return mydb.cursor()