import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["test"]
collections = db["data"]

def get():
    query  = db.collections.find({}).limit(5)
    return query
