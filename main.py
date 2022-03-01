from flask import Flask, render_template, request
# from configparser import ConfigParser
# import os


# config = ConfigParser()
# config.read(os.path.abspath(os.path.join(".ini")))



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/posts")
def posts():
    return "<p>Post Route</p>"
        
@app.route("/user")
def user():
    name = request.args.get('name')
    return render_template('hello.html', name=name)
