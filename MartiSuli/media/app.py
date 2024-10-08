import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify, send_from_directory
from db import DatabaseManager
from model import Base, Szemely, Media, Media_Szerzo, Eloadas, Eloadas_Eloado_Szemely, Eloadas_Blob, Eloadas_Blob_Tipus, Kategoria, Media_Kategoria, Eloadas_Kategoria
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
db_manager = DatabaseManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<string:model_name>', methods=['GET', 'POST'])
@app.route('/api/<string:model_name>/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def api_handler(model_name, id=None):
    model = globals().get(model_name.capitalize())
    if not model:
        return jsonify({"error": "Invalid model name"}), 400

    if request.method == 'GET':
        items = db_manager.select(model, id)
        if id:
            return jsonify(items.to_dict() if items else {})
        else:
            return jsonify([{**item.to_dict_list(), "type": model_name} for item in items])

    elif request.method == 'POST':
        data = request.json
        new_item = model(**data)
        db_manager.add_item(new_item)
        return jsonify(new_item.to_dict()), 201

    elif request.method == 'PUT':
        item = db_manager.get_by_id(model, id)
        if not item:
            return jsonify({"error": "Item not found"}), 404
        data = request.json
        for key, value in data.items():
            setattr(item, key, value)
        db_manager.update_item(item)
        return jsonify(item.to_dict())

    elif request.method == 'DELETE':
        item = db_manager.get_by_id(model, id)
        if not item:
            return jsonify({"error": "Item not found"}), 404
        db_manager.delete_item(item)
        return '', 204

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    search_term = data.get('search_term')
    results = db_manager.select(None, None,  search_term)
    return jsonify(results)

@app.route('/api/<string:model_name>/count', methods=['GET'])
def get_count(model_name):
    model = globals().get(model_name.capitalize())
    if not model:
        return jsonify({"error": "Invalid model name"}), 400
    count = db_manager.get_count(model)
    return jsonify({"count": count})

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
