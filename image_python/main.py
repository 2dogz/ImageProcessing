from flask import Flask, redirect, render_template,alert
from picture_helpers import take_pic
app = Flask(__name__)


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


@app.route('/client')
def client():
    return render_template('client.html', title='Clients')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contacts')

@app.route('/about')
def service():
    return render_template('about.html', title='About')
