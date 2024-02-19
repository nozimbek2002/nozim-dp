from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app)
cluster = MongoClient('mongodb+srv://nurbek:nurbek1205@cluster0.fh6z1.mongodb.net/?retryWrites=true&w=majority')
db = cluster['indivudal']
words_col = db['akt-words']
categories_col = db['akt-categories']


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/categories')
def category():
    return render_template('categories.html')

# API CATEGORIES
def get_last_c_id():
    last_c_id  = categories_col.find().sort([('c_id', -1)]).limit(1)
    try:
        last_c_id = last_c_id[0]['c_id']
    except:
        last_c_id = 0
    return last_c_id

@app.route('/api/categories')
def api_categories():
    # try:
        page = request.args.get('page', 1, int)
        perpage = request.args.get('perpage', 25, int)
        search = request.args.get('search', '', str)

        count = categories_col.count_documents({})
        categories_r = categories_col.find({}).skip(perpage * (page - 1)).limit(perpage)
        categories_list = []
        for item in categories_r:
            categories_list.append({
                "_id": str(item['_id']),
                "c_id": item['c_id'],
                "name": item['name'],
                "fields": item['fields'],
            })
        
        return jsonify(result=categories_list, count=count)
    # except:
    #     return jsonify(False)

@app.route('/api/categories/create', methods=['POST', 'GET'])
def api_create_categories():
    try:
        name = request.json['name']
        fields = request.json['fields']
        last_id = get_last_c_id()+1
        newC = { "c_id": last_id, "name":name, "fields":fields }
        categories_col.insert_one(newC)
        return jsonify(last_id)
    except:
        return jsonify(False)

@app.route('/api/categories/edit/<int:id>', methods=['PUT', 'GET'])
def api_edit_categories(id):
    try:
        name = request.json['name']
        fields = request.json['fields']
        newC = { "name":name, "fields": fields }
        categories_col.update_one({ "c_id": int(id) }, { "$set": newC })
        return jsonify(True)
    except:
        return jsonify(False)

@app.route('/api/categories/delete/<string:id>', methods=['DELETE', 'GET'])
def api_delete_categories(id):
    try:
        categories_col.delete_one({ "c_id": int(id) })
        return jsonify(True)
    except:
        return jsonify(False)


# API WORDS
def get_last_w_id():
    last_w_id  = words_col.find().sort([('w_id', -1)]).limit(1)
    try:
        last_w_id = last_w_id[0]['w_id']
    except:
        last_w_id = 0
    return last_w_id

@app.route('/api/words')
def api_words():
    # try:
        page = request.args.get('page', 1, int)
        perpage = request.args.get('perpage', 25, int)
        category = request.args.get('category', '', int)
        # search = request.args.get('search', '', str)

        count = words_col.count_documents({ "category": category })
        categories_r = words_col.find({ "category": category }).skip(perpage * (page - 1)).limit(perpage)
        categories_list = []
        for item in categories_r:
            del item['_id']
            categories_list.append(item)
        
        return jsonify(result=categories_list, count=count)
    # except:
    #     return jsonify(False)

@app.route('/api/words/create', methods=['POST', 'GET'])
def api_create_words():
    try:
        last_id = get_last_w_id()+1
        words_col.insert_one({"w_id": last_id, **request.json})
        return jsonify({"w_id": last_id, **request.json})
    except:
        return jsonify(False)

@app.route('/api/words/search/<string:name>', methods=['GET'])
def search_words(name):
    regex_pattern = re.compile('^' + name, re.IGNORECASE)
    categories_r = words_col.find_one({ "uzbek": regex_pattern })
    if categories_r:
        del categories_r['_id']
        return jsonify(categories_r)
    return jsonify(False)
    # except:
    #     return jsonify(False)


@app.route('/api/words/edit/<int:id>', methods=['PUT', 'GET'])
def api_edit_words(id):
    try:
        words_col.update_one({ "w_id": int(id) }, { "$set": request.json })
        return jsonify(True)
    except:
        return jsonify(False)

@app.route('/api/words/delete/<string:id>', methods=['DELETE', 'GET'])
def api_delete_words(id):
    try:
        words_col.delete_one({ "w_id": int(id) })
        return jsonify(True)
    except:
        return jsonify(False)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))