import pymongo
from pymongo import MongoClient
from elasticsearch import Elasticsearch
import pprint
from tqdm import tqdm
import warnings

warnings.filterwarnings("ignore")

client = MongoClient("mongodb://mongo:27017/")
db = client["test"]
collections = db["data"]

es1 = Elasticsearch(hosts="elasticsearch", timeout=30, max_retries=10, retry_on_timeout=True)

print("Connected to", es1.info())



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
