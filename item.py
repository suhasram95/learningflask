from flask_restful import reqparse, Resource
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="Name Cannot be blank!")
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Price Cannot be  blank!"
    )

    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if self.find_by_name(name):
            return {'message': 'An item with name {} already exists'.format(name)}, 409
        data = Item.parser.parse_args()
        item = {'name': data['name'], 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {"message": "An error occurred inserting the item"}, 500  # Internal server error

        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES(?, ?)"
        result = cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE FROM items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.close()
        return {'message': 'Item deleted'}, 204

    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message": "An error occured with the item"}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occured with the item"}, 500
        return updated_item, 201


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        rows = result.fetchall()
        connection.close()
        all_items = []
        for row in rows:
            all_items.append(
                {
                    'name': row[0],
                    'price': row[1]
                }
            )
        return {'items': all_items}
