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

# Per fer la connexió s'utilitza el mètode cursor()
connection = conn.cursor()

sql = '''CREATE TABLE USERS(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL,
            user_surname VARCHAR(255) NOT NULL,
            user_age BIGINT NOT NULL,
            user_email VARCHAR(255) NOT NULL
            )'''

print(sql)

connection.execute(sql)
print(connection)