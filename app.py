from flask import Flask
import os
app = Flask(__name__)
store =[
    {
        'name': 'My Wonderful Store',
        'items':[
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]
@app.route('/store', methods=['POST', 'GET'])
def create_store():
    pass

@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

app.run(port=5000)