from flask import Flask, redirect, render_template
from picture_helpers import take_pic
from chess_test import chessboardPicture
from find_contours import contoursPicture
from find_size import *
import os


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route('/')
def index():
    return render_template('index.html', title='Welcome')


@app.route('/newPicture')
def newPicture():
    try:
        take_pic()
        #chessboardPicture()
        #contoursPicture()
        #size_find_v1()
    except Exception as e:
        print(e)
    return redirect("/", code=302)


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
    app.run(debug=True, host='0.0.0.0')
