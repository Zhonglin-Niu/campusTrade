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

# users[max(users.keys())+1] = User.add(max(users.keys())+1, "Zachariah Jia Tester", "zj23@calvin.edu", "password")

# DUMP categories
with open('category.json', 'w+') as f:
    json.dump([category.to_json() for category in categories.values()], f)


# DUMP tags
with open('tags.json', 'w+') as f:
    json.dump([tag.to_json() for tag in tags.values()], f)

# DUMP users
with open('users.json', 'w') as f:
    json.dump([user.to_json() for user in users.values()], f)

# # DUMP items
with open('data.json', 'w') as f:
    json.dump([item.to_json() for item in items.values()], f)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/items")
def get_items():
    return jsonify([item.to_json() for item in items.values()])

@app.route("/add_item", methods=['POST'])
def add_item():
    data = request.get_json()
    id = data.get('id')
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

    if not all([id, title, description, price, cover, images, created, category, tags, status, owner]):
        return jsonify({"error": "Missing data"}), 400

    item = Item.add(id, title, description, price, cover, images, created, updated, category, tags, status, owner)
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

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    id = data.get('id')
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


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="::")
