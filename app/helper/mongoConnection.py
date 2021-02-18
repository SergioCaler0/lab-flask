from pymongo import MongoClient

client = MongoClient()

celebrities = client.Hollywood.celebrities
movies = client.Hollywood.movies

def insert_celebritie(celebritie):
    res = celebrities.insert_one(celebritie)
    return res.inserted_id


#insert_celebritie({"name":"Samuel L. Jackson"})
