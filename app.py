from flask import Flask
import os
app = Flask(__name__)

hello = "Hello, world! This is from the program I am using flask"
@app.route('/')
def home():
    return hello

app.run(port=5000)