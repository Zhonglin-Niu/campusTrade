from flask import Flask, render_template
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
categories = {category['id']: category['name'] for category in data}

# LOAD tags
with open('tags.json', 'r') as f:
    data = json.load(f)
tags = {tag['id']: tag['name'] for tag in data}

# LOAD users
with open('users.json', 'r') as f:
    data = json.load(f)
users = {user['id']: user['name'] for user in data}
########## END OF LOADING ##########

print()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_data")
def get_data():

    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
