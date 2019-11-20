from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['GUI']
db.authenticate(name="admin", password="  ")
collection = db["users"]
for posts in collection.find():
    print(posts)