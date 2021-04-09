import pymongo  # package for working with MongoDB
from bson import json_util
import json

client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["test"]
collections = db["data"]

with open('2feed1food-data.json', 'r') as myfile:
    file=myfile.read()

data = json.loads(file)
db.collections.insert_many(data)
