from flask import Flask
from flask_socketio import SocketIO

from wsb.config import Config
from wsb.scripts.reddit_scraper import Scraper

app = Flask(__name__)
app.config.from_object(Config)


from wsb.main.routes import main

app.register_blueprint(main)
socketio = SocketIO(app, cors_allowed_origins='*') #  async_mode='threading'

# This code surely needs to go somewhere else
@socketio.on('client_connected')
def handle_client_connect_event(data):
    print("connected")
    print(str(data))    
@socketio.on('disconnect')
def disconnected():
    print('disconnected')
@socketio.on('connect')
def connected():
    print('connected')
    

scraper = Scraper(socketio)
