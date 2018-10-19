import os
from flask import Flask, request
from twitter import twitter_api



app = Flask(__name__)
app.register_blueprint(twitter_api)
# app.wsgi_app = middleEarth.simpleMiddleWare(app.wsgi_app) ini dikomen biar gaya aja mau coba yg before request


@app.route('/')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True , host='localhost', port=8000)