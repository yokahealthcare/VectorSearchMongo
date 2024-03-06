import os

import pymongo
from dotenv import load_dotenv
from tqdm import tqdm
load_dotenv()

import util

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = client.sample_mflix
collection = db.movies

for doc in tqdm(collection.find({"plot": {"$exists": True}})):
    plot = doc["plot"]
    vector_embedding = util.generate_embedding_hf(plot)

    doc["plot_embedding_hf"] = vector_embedding
    collection.replace_one({"_id": doc["_id"]}, doc)
