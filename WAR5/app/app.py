from flask import Flask, redirect, render_template
from flask_mysqldb import MySQL
from cv_files.picture_helpers import take_pic
from cv_files.chess_test import chessboardPicture
from cv_files.find_contours import contoursPicture
from cv_files.find_size import *
import os
import base64
import psycopg2

app = Flask(__name__)
# conn = psycopg2.connect(
#     host="127.0.0.1",
#     database="test_db",
#     user="user",
#     password="password123")

mysql = MySQL(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'kyle'
app.config['MYSQL_PASSWORD'] = 'An0thrS3crt'
app.config['MYSQL_DB'] = 'test_db'


@app.route('/')
def index():
    return render_template('index.html', title='Welcome')


@app.route('/newPicture')
def newPicture():
    try:
        take_pic()
    except Exception as e:
        print(e)
    return redirect("/", code=302)

@app.route('/newPictureContours')
def newPictureContours():
    try:
        contoursPicture()
    except Exception as e:
        print(e)
    return redirect("/", code=302)

@app.route('/newPictureChess')
def newPictureChess():
    try:
        chessboardPicture()
    except Exception as e:
        print(e)
    return redirect("/", code=302)

@app.route('/newPictureSize')
def newPictureSize():
    try:
        size_find_v1("static/photos/proper_env.png")
    except Exception as e:
        print(e)
    return redirect("/", code=302)

@app.route('/image/<int:id>')
def image(id):
    retrieve_query = f"SELECT * FROM Images WHERE ID = {id}"
    cursor = mysql.connection.cursor()
    cursor.execute(retrieve_query.format(str(id)))
    result = cursor.fetchone()
    #image = base64.b64encode(result[2]).decode("utf-8")
    image = result[2]
    title = result[1]
    return render_template('images.html', img_title=title, img_data=image)

@app.route('/images-postgres/')
def images():
    retrieve_query = "SELECT * FROM Images WHERE ID = 1"
    cursor = conn.cursor()
    #cursor = mysql.connection.cursor()
    cursor.execute(retrieve_query.format(str(1)))
    result = cursor.fetchone()
    image = base64.b64encode(result[2])
    #image = result[0]
    print(result[2])
    title = result
    return render_template('images.html', img_title=title, img_data=image)

@app.route('/client')
def client():
    return render_template('client.html', title='Clients')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contacts')

@app.route('/about')
def service():
    return render_template('about.html', title='About')


@app.route('/photos')
def photos():
    imgs = os.listdir(os.path.join(app.static_folder, "photos"))
    return render_template('photos.html', images=imgs)

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
