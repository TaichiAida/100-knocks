# coding utf-8
# MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．

#####################
# インタラクティブシェル
#####################
# mongo     # 起動
# show dbs  # DBの確認
"""
admin             0.000GB
artists_database  0.385GB
artists_db        0.135GB
config            0.000GB
local             0.000GB
"""
# use artists_db      # 使うDBを選択、移動
"""
switched to db artists_db
"""
# show collections          # DB内のcollectionsを確認
"""
artists
"""
# db.artists.find({"area":"Japan"}).count()     # db.find()まで65と同じ。count()で要素数をカウントできる
"""
22821
"""
# exit      # 終了
"""
bye
"""
