import sys
sys.path.append("../")
from app import app
from flask import request
from bson import json_util
from helper.mongoConnection import insert_celebritie

@app.route("/")
def create_celebritie():
    celebritie = request.args
    id_ = insert_celebritie(celebritie)


    return json_util.dumps(id_)
    #return {"Welcome": "to datamad0121 API!!!"}

