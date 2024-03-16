# This file stores the user information as a Class
import json
from datetime import datetime

# Define the Base class
class Base:
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    def to_json(self):
        # Convert the instance to a JSON string
        # Use the json_default method to handle datetime objects
        return json.dumps(self.__dict__, default=self.json_default)

    @classmethod
    def from_json(cls, json_str):
        # Convert a JSON string to a dictionary and create a new instance
        return cls(**json.loads(json_str))
    
    def json_default(self, obj):
        # Convert datetime objects to strings
        if isinstance(obj, datetime):
            return obj.strftime(self.DATE_FORMAT)
        # Raise an error if obj is not serializable
        raise TypeError(f"Type {type(obj)} not serializable")

# Define the User class
class User(Base):
    def __init__(self, id:int, name:str, email:str, password:str, created:str, last_login:str, status:str, role:str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.created = created
        self.last_login = last_login
        self.status = status
        self.role = role

# Define the Category class
class Category(Base):
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name

# Define the Item class
class Item(Base):
    # Define the date format used in the JSON data
    def __init__(self, id:int, title:str, description:str, price:float, cover:str, images:list[str], created:str, updated:str, category:list[str], tags:list[str], status:str, owner:str):
        # Assign all the fields from the JSON data to instance variables
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.cover = cover
        self.images = images
        # Convert the date strings to datetime objects
        self.created = datetime.strptime(created, self.DATE_FORMAT)
        self.updated = datetime.strptime(updated, self.DATE_FORMAT)
        self.category = category
        self.tags = tags
        self.status = status
        self.owner = owner