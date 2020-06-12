import os

from flask import Flask, url_for, render_template, request, redirect, flash

from flask_socketio import SocketIO, emit

app = Flask(__name__)


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


# Channel List
channel_list = []


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', channel_list=channel_list)

@socketio.on('emit_newchannel')
def proc(data):
    newchannel = data['newchannel']
    channel_list.append(newchannel)
    emit('response', {'resp_newchannel': channel_list}, broadcast=True)
