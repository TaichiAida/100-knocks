# coding utf-8
# アーティスト情報（artist.json.gz）をデータベースに登録せよ．
# さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value

import gzip
import json
from pymongo import MongoClient
import pymongo

# default port number is "27017"
client = MongoClient("mongodb://localhost:27017")
#client = MongoClient()

# 何回もやるとデータが重複する！
#db = client.artists_database

# artists_databaseを3、4回やって66、68の結果が重複したため、こちらが本命
db = client.artists_db
collection = db.artists

"""
collection_name = db["name"]
collection_aliases_name = db["aliases.name"]
collection_tags_value = db["tags.value"]
collection_rating_value = db["rating.value"]
"""

count = 0   # 今回だけの終了条件
with gzip.open("artist.json.gz") as data:
    # ある程度まとめておくためのいれもの
    mid = []
    for line in data:
        dic = json.loads(line)
        # insert_one だと時間がかかる。
        # ある程度まとめてinsert_manyを使うと良さそう
        #collection.insert_one(dic)
        mid.append(dic)
        count += 1
        # まとまったらinsert_many, mid初期化
        if len(mid) >= 100000:
            collection.insert_many(mid)
            mid = []
            print(f"{count}件追加完了")
    # 残りの1337件をここで追加する
    if len(mid) > 0:
        collection.insert_many(mid)
        mid = []
print(f"{count}件追加完了")

# インデックス作成。ASCENDING：昇順
collection.create_index([("name", pymongo.ASCENDING)])  
collection.create_index([("aliases.name", pymongo.ASCENDING)])  
collection.create_index([("tags.value", pymongo.ASCENDING)])
collection.create_index([("rating.value", pymongo.ASCENDING)])
