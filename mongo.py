
import os
import pymongo


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myRecipe"
COLLECTION = "recipies"
USERS = "members"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect: %s") % e


conn = mongo_connect(MONGO_URI)

recipes = conn[DATABASE][COLLECTION]
users = conn[DATABASE][USERS]

posts = recipes.find()
records = users.find()

for post in posts:
    print(post)

for record in records:
    print(record)
