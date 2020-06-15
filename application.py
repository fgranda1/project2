import os

from flask import Flask, url_for, render_template, request, redirect, flash, jsonify

from flask_socketio import SocketIO, emit

app = Flask(__name__)


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


# Channel List
channel_list = ['general']

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', channel_list=channel_list)

@app.route("/room/<roomname>")
def chatroom(roomname):
    return render_template('room.html', roomname=roomname)

@socketio.on('emit_newchannel')
def proc(data):
    newchannel = data['newchannel']
    newchannel = newchannel.lower()
    if newchannel in channel_list:
        error = 'exist'
        emit('response', {'resp_newchannel': error}, broadcast=False)
    else:
        channel_list.append(newchannel)
        emit('response', {'resp_newchannel': channel_list}, broadcast=True)
