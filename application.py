import os

from flask import Flask, url_for, render_template, request, redirect, flash

from flask_socketio import SocketIO, emit

app = Flask(__name__)


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


nick_name_list = []

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', nick_name_list=nick_name_list )
