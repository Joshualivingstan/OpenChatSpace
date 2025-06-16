from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["OpenChatSpace"]
messages_collection = db["messages"]
