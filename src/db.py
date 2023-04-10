import pymongo

from pymongo.collection import Collection
from typing import Dict

from settings import DB_NAME, COLLECTION_NAME, GROUP_TYPES


def get_collection() -> Collection:
    """Получаем коллекцию, с которой будем работать."""
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient[DB_NAME]
    colllection = db[COLLECTION_NAME]
    return colllection


def get_aggregation(
        collection: Collection, request: Dict
) -> Collection:
    """Получаем агрегированную коллекцию."""
    aggregate_collection = collection.aggregate([
        {
            '$match': {
                'dt': {
                    '$gte': request['dt_from'], '$lte': request['dt_upto']
                }
            }
        },
        {
            '$group': {
                '_id': {'$dateToString': GROUP_TYPES[request['group_type']]},
                'total_value': {'$sum': '$value'}
            }
        },
        {'$sort': {'_id': 1}},
        {
            '$project': {
                '_id': 0,
                'label': '$_id',
                'value': '$total_value'
            }
        }
    ])
    return aggregate_collection
