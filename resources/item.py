from flask_restful import reqparse, Resource
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Price Cannot be  blank!")
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every item needs a store id"
    )

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name {} already exists'.format(name)}, 409
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500  # Internal server error

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item Deleted'}, 204
        return {'message': 'Item not found'}, 404

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, **data)

        if item is None:
            try:
                updated_item.insert(updated_item)
            except:
                return {"message": "An error occurred with the item"}, 500
        else:
            try:
                updated_item.update(updated_item)
            except:
                return {"message": "An error occurred with the item"}, 500
        return updated_item, 201


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
