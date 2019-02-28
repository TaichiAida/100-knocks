# coding utf-8
# "dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．

import json
import pymongo
from pymongo import MongoClient

# default port number is "27017"
client = MongoClient("mongodb://localhost:27017")
db = client.artists_db
collection = db.artists

# "dance"というタグが付与されたアーティストを検索
dancers = collection.find({"tags.value": "dance"})

# 投票数で並べる。DESCENDING：降順
dancers.sort("rating.count", pymongo.DESCENDING)

# 10件表示
count = 0
for dancer in dancers:
    #print(dancer)
    if "rating" in dancer:
        rating = dancer["rating"]["count"]
    # "dance"がタグつけられたアーティスト数は286
    # そのうちの168は投票されていない　-> Noneとすべき
    else:
        rating = "None"
    print(f"{dancer['name']}(id:{dancer['id']})\t{rating}")
    count += 1
    if count >= 10:
        break