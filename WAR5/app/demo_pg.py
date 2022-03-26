import psycopg2
import base64

conn = psycopg2.connect(
    host="127.0.0.1",
    database="test_db",
    user="user",
    password="password123")


def createTable():
    create_query = "CREATE TABLE Images ( id SERIAL PRIMARY KEY, name VARCHAR(20), photo bytea );"
    cursor.execute(create_query)
    conn.commit()

# create a cursor
cursor = conn.cursor()

# execute a statement
print('PostgreSQL database version:')
cursor.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cursor.fetchone()
print(db_version)




def insertBlob(FilePath, name):
    with open(FilePath, 'rb') as File:
        BinaryData = base64.b64encode(File.read())
    insert_query = "INSERT INTO Images (name, photo) VALUES (%s, %s)"
    cursor.execute(insert_query, (str(name), BinaryData))
    conn.commit()


def retrieveBlob(ID):
    retrieve_query = "SELECT * FROM Images WHERE ID = '{0}'"
    cursor.execute(retrieve_query.format(str(ID)))
    result = cursor.fetchone()[2]
    print(type(result))
    print(base64.b64encode(result).decode("utf-8"))


def main():
    createTable()
    insertBlob("static/photos/kw_aruco_envelope.jpg", "kw_test")
    retrieveBlob(1)
    # close the communication with the PostgreSQL
    cursor.close()

if __name__ == '__main__':
    main()
