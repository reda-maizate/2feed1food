import pymongo  # package for working with MongoDB
from pymongo import MongoClient
import json
from elasticsearch import Elasticsearch
from tqdm import tqdm
import warnings

warnings.filterwarnings("ignore")

print("LOG: Connection to the Mongo Database!")

client = MongoClient("mongodb://mongo:27017/")
db = client["test"]
collections = db["data"]

print("LOG: Succesfully connected to the Mongo Database!")
print("LOG: Adding data on the Mongo Database!")

with open('2feed1food-data.json', 'r') as myfile:
    file=myfile.read()

data = json.loads(file)
db.collections.insert_many(data)

print("LOG: Succesfully added data to the Mongo Database!")
print("LOG: Connection to the Elasticsearch Database!")

es1 = Elasticsearch(hosts="elasticsearch", timeout=30, max_retries=10, retry_on_timeout=True)

print("LOG: Succesfully connected to the Elasticsearch Database!")
print("LOG: Adding the Mongo data on Elasticsearch!")

actions = []
for data in tqdm(db.collections.find(), total=db.collections.count()):
    data.pop("_id")
    action = {
              "index": {
                  "_index": "test",
                  "_type": "data",
              }
    }
    actions.append(action)
    actions.append(data)

request_body = {
    "settings" : {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}

es1.indices.create(index='test', body=request_body, ignore=400)
es1.bulk(index="test", body=actions, refresh=True)
print("LOG: Succesfully added to the Elasticsearch Database!")
