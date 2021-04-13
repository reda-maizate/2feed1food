import pymongo
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from tqdm import tqdm
import warnings

client = MongoClient("mongodb://mongo:27017/")
db = client["test"]
collections = db["data"]

es1 = Elasticsearch(hosts="elasticsearch", timeout=30, max_retries=10, retry_on_timeout=True)
