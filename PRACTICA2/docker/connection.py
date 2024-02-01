import psycopg2

# Per saber quina és la database, el user i el password mirar el .yml
conn = psycopg2.connect(
    database="",
    user="",
    password="",
    host="",
    host="localhost",
    port="5432"
)


