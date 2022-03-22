import mysql.connector

# SET PASSWORD FOR root@localhost=PASSWORD('mypassword')

mydb = mysql.connector.connect(
  host="127.0.0.1",
  database="citizix_db",
  user="root",
  port=32000,
  password="S3cret"
)

# def grant_privs():
#     cursor = mydb.cursor(buffered=True)
#     cursor.execute("GRANT ALL PRIVILEGES ON knights.* TO 'citizix_user'@'localhost'")
#
# grant_privs()
cursor = mydb.cursor(buffered=True)
if mydb:
    cursor.execute("SHOW tables")
    tables_exist = cursor.rowcount
    if not tables_exist:
        try:
            cursor.execute("CREATE DATABASE knights")
        except:
            pass
        try:
            cursor.execute("CREATE TABLE favorite_colors ( \
                            name VARCHAR(20), \
                            color VARCHAR(10) \
                            );")
        except:
            pass
    cursor.execute("INSERT INTO favorite_colors \
                    (name, color) \
                    VALUES \
                    ('Lancelot', 'blue'), \
                    ('Galahad', 'yellow'); \
                    ")
    cursor.execute("select * from favorite_colors")
    records = cursor.fetchall()
    print(records)
else:
    print('ERROR - DATABASE CONNECTION')
    print(mydb)
