from flask import Flask, redirect, render_template
from picture_helpers import take_pic
from chess_test import chessboardPicture
from find_contours import contoursPicture
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Welcome')


@app.route('/newPicture')
def newPicture():
    try:
        #take_pic()
        #chessboardPicture()
        contoursPicture()
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
