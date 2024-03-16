# This file stores the user information as a Class
import json
from datetime import datetime

# Define the Base class
class Base:
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


    @classmethod
    def from_json(cls, json_str):
        # Convert a JSON string to a dictionary and create a new instance
        return cls(**json.loads(json_str))
    
    @classmethod
    def add(cls, *args, **kwargs):
        # Create a new instance of the class and return it
        return cls(*args, **kwargs)
    
    @classmethod
    def delete(cls, id, data_store):
        if id in data_store:
            del data_store[id]
        else:
            raise ValueError(f"No {cls.__name__} with id {id} found.")

    def to_json(self):
        return self.__dict__
    
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
    
    def add(self, id:int, name:str, email:str, password:str, role:str = "user"):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.created = datetime.now().strftime(self.DATE_FORMAT)
        self.last_login = datetime.now().strftime(self.DATE_FORMAT)
        self.status = "active"
        self.role = role

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
        self.created = created
        self.updated = updated
        self.category = category
        self.tags = tags
        self.status = status
        self.owner = owner
    
    def update_item(self, id:int, title:str, description:str, price:float, cover:str, images:list[str], category:list[str], tags:list[str], status:str, owner:str):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.cover = cover
        self.images = images
        self.updated = datetime.now().strftime(self.DATE_FORMAT)
        self.category = category
        self.tags = tags
        self.status = status
        self.owner = owner

# Define the Category class
class Category(Base):
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name

# Define the Tag class
class Tag(Base):
    def __init__(self, id:int, name:str, subtags:list[str] = []):
        self.id = id
        self.name = name
        self.subtags = subtags

