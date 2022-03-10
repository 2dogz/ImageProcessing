from flask import Flask, redirect, render_template
from picture_helpers import take_pic
from chess_test import chessboardPicture
from find_contours import contoursPicture
import os


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must- \
    revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
