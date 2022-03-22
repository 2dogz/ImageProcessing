import mysql.connector
import base64
# SET PASSWORD FOR root@localhost=PASSWORD('mypassword')

mydb = mysql.connector.connect(
  host="127.0.0.1",
  database="test_db",
  user="root",
  port=32000,
  password="S3cret"
)


cursor = mydb.cursor(buffered=True)


def insertBlob(FilePath, name):
    with open(FilePath, 'rb') as File:
        BinaryData = base64.b64encode(File.read())
    insert_query = "INSERT INTO Images (name, photo) VALUES (%s, %s)"
    cursor.execute(insert_query, (str(name), BinaryData))
    mydb.commit()


def retrieveBlob(ID):
    retrieve_query = "SELECT * FROM Images WHERE ID = '{0}'"
    cursor.execute(retrieve_query.format(str(ID)))
    result = cursor.fetchone()[2]
    print(type(result))
    print(base64.b64encode(result).decode("utf-8"))
    #print(result)

    #StoreFilePath = "static/db_photos/img{0}.jpg".format(str(ID))
    #with open(StoreFilePath, "wb") as File:
    #    File.write(result)
    #    File.close()

def main():
    insertBlob("static/photos/kw_aruco_envelope.jpg", "kw_test")
    retrieveBlob(1)

if __name__ == '__main__':
    main()
