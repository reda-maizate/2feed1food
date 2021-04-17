import pymongo  # package for working with MongoDB
from tqdm import tqdm
import json
import sys
import warnings
import os
from mongoosastic.mongoosastic import *
import openfoodfacts
import shutil
import tarfile

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

warnings.filterwarnings("ignore")

print("LOG: Adding data on the Mongo Database!")

if "-light" in opts:
    with open('notebook/mongoDB/2feed1food-light.json', 'r') as myfile:
        file=myfile.read()

    data = json.loads(file)
    db.collections.insert_many(data)
    print("LOG: Installation of the light version done!")
elif "-full" in opts:
    with open('notebook/mongoDB/2feed1food-full.json', 'r') as myfile:
        file=myfile.read()

    data = json.loads(file)
    db.collections.insert_many(data)
    print("LOG: Installation of the full version done!")
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-light | -full)")

print("LOG: Succesfully added data to the Mongo Database!")
