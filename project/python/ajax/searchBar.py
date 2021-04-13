import json

import pymongo


def get_item(res):
    mongo = pymongo.MongoClient("mongodb://mongo:27017/")
    data = mongo.test.data

    result = data.find_one(
        # {
        #     "name": {"$regex": "*+p*+"}
        # },
        # {
        #     "protein_100g": 1, "_id": 0
        # }
    )
    return json.dumps(result)


    pass
    data_cols = ['red', 'blue', 'black', 'white', 'green']
    return {
        'labels': data_cols,
        'data': {
            'data': data_set,
            'label': 'test',
            'backgroundColor': '#3AF'
        }
    }
