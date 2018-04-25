from pymongo import MongoClient

client = MongoClient()
db = client['projekt']

db.kindle.drop()
