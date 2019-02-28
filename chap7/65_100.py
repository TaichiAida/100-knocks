# coding utf-8
# MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
# さらに，これと同様の処理を行うプログラムを実装せよ．


#####################
# インタラクティブシェル
#####################
# 基本的にshowとuseしか使わないのかも
# mongo     # 起動
# show dbs  # 確認
"""
admin             0.000GB
artists_database  0.385GB
config            0.000GB
local             0.000GB
"""
# use artists_database  # 使用するデータベースへ移動
"""
switched to db artists_db
"""
# show collections
"""
artists
"""
# db.artists.find( { "name": "Queen" } );
"""
（情報検索完了）
"""
# exit      # 終了
"""
bye
（終了される）
"""


############################
# 上の処理をプログラムで実行する
############################
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

# default port number is "27017"
client = MongoClient("mongodb://localhost:27017")
db = client.artists_db
collection = db.artists

# ObjectIdをなんとかするための関数
def changeObjectId(obj):
    if type(obj) == ObjectId:
        return str(obj)     # 文字列として扱う
    #raise TypeError(repr(obj) + " is not JSON serializable")


# インタラクティブシェルと同じように検索できる
for dic in collection.find({"name":"Queen"}):

    # そのまま出力すると、1行になって見辛い
    #print(dic)

    # json.dumpsの内部をいじるといい感じになりそうだが、以下のエラー。
    # ObjectId：MongoDBにおける識別子
    """
    TypeError: Object of type 'ObjectId' is not JSON serializable
    """
    # 辞書をdumpしてDBに登録　OK
    # DBから辞書を取り出してdump　NG　らしい
    #print(json.dumps(dic,ensure_ascii=False,indent=4,sort_keys=True))

    # ObjectIdを意識する必要がある
    # 上のchangeObjectIdで解消
    print(json.dumps(dic,ensure_ascii=False,indent=4,sort_keys=True,default=changeObjectId))
