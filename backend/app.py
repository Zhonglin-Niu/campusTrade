from flask import Flask, render_template, request, jsonify
from class_def import *
import json

app = Flask(__name__)

########## LOADING DATA ##########
# LOAD ITEMS
with open('data.json', 'r') as f:
    data = json.load(f)
items = {item['id']: Item.from_json(json.dumps(item)) for item in data}

# LOAD categories
with open('category.json', 'r') as f:
    data = json.load(f)
categories = {category['id']: Category.from_json(json.dumps(category)) for category in data}
# categories = {category['id']: category['name'] for category in data}

# LOAD tags
with open('tags.json', 'r') as f:
    data = json.load(f)
tags = {tag['id']: Tag.from_json(json.dumps(tag)) for tag in data}

# LOAD users
with open('users.json', 'r') as f:
    data = json.load(f)
users = {user['id']: User.from_json(json.dumps(user)) for user in data}
########## END OF LOADING ##########

# SAVE ALL
@app.route("/save")
def save():
    # DUMP categories
    with open('category.json', 'w+') as f:
        json.dump([category.to_json() for category in categories.values()], f, ensure_ascii=False, indent=4)
    # DUMP tags
    with open('tags.json', 'w+') as f:
        json.dump([tag.to_json() for tag in tags.values()], f, ensure_ascii=False, indent=4)
    # DUMP users
    with open('users.json', 'w') as f:
        json.dump([user.to_json() for user in users.values()], f, ensure_ascii=False, indent=4)
    # DUMP items
    with open('data.json', 'w') as f:
        json.dump([item.to_json() for item in items.values()], f, ensure_ascii=False, indent=4)
    return jsonify({"message": "Done!"}), 200

#################### ITEMS ####################
@app.route("/items")
def get_items():
    return jsonify([item.to_json() for item in items.values()])

@app.route("/item/<int:id>")
def get_item(id):
    if id not in items:
        return jsonify({"error": "Item not found"}), 404
    
    return jsonify(items[id].to_json())

@app.route("/add_item", methods=['POST'])
def add_item():
    data = request.get_json()
    id = max(items.keys(),default=0) + 1
    title = data.get('title')
    description = data.get('description')
    price = data.get('price')
    cover = data.get('cover')
    images = data.get('images')
    created = datetime.now().strftime(Item.DATE_FORMAT)
    updated = created
    category = data.get('category')
    tags = data.get('tags')
    status = data.get('status')
    owner = data.get('owner')

    if not all([id, title, description, price, cover, category, status, owner]):
        return jsonify({"error": "Missing data"}), 400

    item = Item.add(id, title, description, price, cover, images, created, updated, category, tags, status, owner)
    items[id] = item
    return jsonify(item.to_json()), 201

@app.route("/remove_item/<int:id>", methods=['DELETE'])
def remove_item(id):
    if id not in items:
        return jsonify({"error": "Item not found"}), 404

    del items[id]
    return jsonify({"message": "Item removed"}), 200

# Modify/Update item information
@app.route("/update_item/<int:id>", methods=['PATCH'])
def update_item(id):
    if id not in items:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    item = items[id]
    item.title = data.get('title', item.title)
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)
    item.cover = data.get('cover', item.cover)
    item.images = data.get('images', item.images)
    item.updated = datetime.now().strftime(Item.DATE_FORMAT)
    item.category = data.get('category', item.category)
    item.tags = data.get('tags', item.tags)
    item.status = data.get('status', item.status)
    item.owner = data.get('owner', item.owner)
    item.update_item(id, item.title, item.description, item.price, item.cover, item.images, item.category, item.tags, item.status, item.owner)
    return jsonify(item.to_json()), 200

#################### Users ####################
@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    id = max(users.keys(),default=0) + 1
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not all([id, name, email, password]):
        return jsonify({"error": "Missing data"}), 400

    for u in users.values():
        if u.email == email:
            return jsonify({"error": "Email already exists"}), 400

    user = User.add(id, name, email, password)
    return jsonify(user.to_json()), 201

# remove user.
@app.route("/remove_user/<int:id>", methods=['DELETE'])
def remove_user(id):
    if id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[id]
    return jsonify({"message": "User removed"}), 200

# deactivate user
@app.route("/deactivate_user/<int:id>", methods=['PATCH'])
def deactivate_user(id):
    if id not in users:
        return jsonify({"error": "User not found"}), 404

    user = users[id]
    user.status = "unactive"
    return jsonify(user.to_json()), 200

#################### Categories ####################
@app.route("/categories")
def get_categories():
    return jsonify([category.to_json() for category in categories.values()])

@app.route("/category/<int:id>")
def get_category(id):
    if id not in categories:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(categories[id].to_json())

#################### Tags ####################
@app.route("/tags")
def get_tags():
    return jsonify([tag.to_json() for tag in tags.values()])

@app.route("/tag/<int:id>")
def get_tag(id):
    if id not in tags:
        return jsonify({"error": "Tag not found"}), 404
    return jsonify(tags[id].to_json())

if __name__ == "__main__":
    app.run(debug=True, port=80, host="::")
