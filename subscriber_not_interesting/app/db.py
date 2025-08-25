"""
mow are it connect mongodb for the "not_interesting" subscriber
"""

from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["newsgroups"]
collection = db["not_interesting"]