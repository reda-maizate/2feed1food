import pymongo
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from tqdm import tqdm
import warnings

print("LOG: Connection to the Mongo Database!")
client = MongoClient("mongodb://mongo:27017/?replicaSet=replica0")
db = client["off"]
collections = db["collections"]
print("LOG: Succesfully connected to the Mongo Database!")

print("LOG: Connection to Elastic!")
es1 = Elasticsearch(hosts="elasticsearch", timeout=30, max_retries=10, retry_on_timeout=True)
print("LOG: Succesfully connected to Elastic!")
