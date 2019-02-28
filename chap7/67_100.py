# coding utf-8
# 特定の（指定した）別名を持つアーティストを検索せよ．

import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# 基本的には65と同じ。

# default port number is "27017"
client = MongoClient("mongodb://localhost:27017")
db = client.artists_database
collection = db.artists

# ObjectIdをなんとかするための関数
def changeObjectId(obj):
    if type(obj) == ObjectId:
        return str(obj)     # 文字列として扱う

name = input()

for dic in collection.find({"aliases.name": name}):
    print(json.dumps(dic,ensure_ascii=False,indent=4,sort_keys=True,default=changeObjectId))

