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
    with open('mongoDB/2feed1food-data.json', 'r') as myfile:
        file=myfile.read()

    data = json.loads(file)
    db.collections.insert_many(data)
    print("LOG: Installation of the light version done!")
elif "-full" in opts:
    # Not the best solution, reflection on going.. 
    print("LOG: Starting download of the data! (The download can takes more than 10mn)")
    openfoodfacts.utils.download_data() # This file is X.XXGb.
    print("LOG: Data downloaded!")

    print("LOG: Moving the data to the mongo directory!")
    shutil.move("openfoodfacts-mongodbdump.tar.gz", "../data/mongo/openfoodfacts-mongodbdump.tar.gz")
    print("LOG: Succesfully moved the data to the mongo directory!")

    os.chdir("../data/mongo")
    print("LOG: Changed directory, now in /data/mongo/")

    tar = tarfile.open("openfoodfacts-mongodbdump.tar.gz", "r:gz")
    print("LOG: Extracting starting! (The extraction can takes more than 10mn)")
    tar.extractall()
    print("LOG: Extracting finished!")
    tar.close()

    os.remove("openfoodfacts-mongodbdump.tar.gz")
    print("LOG: openfoodfacts-mongodbdump.tar.gz deleted!")
    print("-----------------------------")
    print("# MANUAL COMMAND TO EXECUTE #")
    print("To finish the installation:")
    print("- Open a new command line and run 'docker exec -it mongo bash'")
    print("- To restore the full database, run 'mongorestore /data/db/dump'")
    print("- Wait until the end of the execution.")
    print("----------------------------")
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-light | -full)")

print("LOG: Succesfully added data to the Mongo Database!")
