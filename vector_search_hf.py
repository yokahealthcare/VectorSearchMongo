import os

import pymongo
from dotenv import load_dotenv

load_dotenv()

import util

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client.sample_mflix
collection = db.movies


query = "imaginary characters from outer space at war"
results = collection.aggregate([
    {"$vectorSearch": {
        "queryVector": util.generate_embedding_hf(query),
        "path": "plot_embedding_hf",
        "numCandidates": 100,
        "limit": 4,
        "index": "PlotSemanticSearch", }}
])

for document in results:
    print(f"Movie Name: {document['title']}, \nMovie Plot: {document['plot']}\n")
