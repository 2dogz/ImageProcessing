import mysql.connector
import base64

def user_db():
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="kyle",
      port=3306,
      password="An0thrS3crt"
    )
    return mydb

def admin_db():
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      port=3306,
      password="S3cret"
    )
    return mydb

admin = admin_db()
non_admin = user_db()
cursor = non_admin.cursor(buffered=True)

cursor.execute("SHOW DATABASES;")
result = cursor.fetchall()
print(result)

cursor.execute("USE test_db;")


def createTable():
    create_query = "CREATE TABLE IF NOT EXISTS Images ( \
                     id MEDIUMINT NOT NULL AUTO_INCREMENT, \
                     name CHAR(30) NOT NULL, \
                     image LONGBLOB, \
                     PRIMARY KEY (id) \
                     );"
    cursor.execute(create_query)
    non_admin.commit()

def insertBlob(FilePath, name):
    with open(FilePath, 'rb') as File:
        BinaryData = base64.b64encode(File.read())
    insert_query = "INSERT INTO Images (name, image) VALUES (%s, %s)"
    cursor.execute(insert_query, (str(name), BinaryData))
    non_admin.commit()


def retrieveBlob(ID):
    retrieve_query = "SELECT * FROM Images WHERE ID = '{0}'"
    cursor.execute(retrieve_query.format(str(ID)))
    result = cursor.fetchone()[2]
    print(type(result))
    print(result)
    #print(base64.b64encode(result).decode("utf-8"))

def main():

    createTable()
    cursor.execute("SHOW Tables;")
    result = cursor.fetchall()
    print(result)
    insertBlob("static/photos/kw_aruco_envelope.jpg", "kw_test")
    retrieveBlob(1)
    # close the communication with mySQL
    cursor.close()

if __name__ == '__main__':
    main()
