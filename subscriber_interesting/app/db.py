"""
now hare mongodb connection for the "interesting" subscriber
"""

from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client["newsgroups"]
collection = db["interesting"]