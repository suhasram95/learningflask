from flask import Flask
import os
app = Flask(__name__)

hello = "Hello, world! This is from the program I am using flask"
@app.route('/store', methods=['POST', 'GET'])
def create_store():
    pass

@app.route('/store/<string:name>', methods=['GET'])
def get_store():
    pass

def 

app.run(port=5000)