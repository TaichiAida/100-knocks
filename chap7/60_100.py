# coding utf-8
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．

# KVS:LevelDB, Redis, KyotoCabinet, memchaed, Big Table

# dic["アーティスト名(name)"] = "活動場所(area)"
import json
import gzip
import plyvel

db = plyvel.DB("./db_60/", create_if_missing=True)
with gzip.open("artist.json.gz") as data:
    for line in data:
        dic = json.loads(line)
        if "name" in dic and "area" in dic:
            db.put(dic["name"].encode("utf-8"), dic["area"].encode("utf-8"))
# 確認用
print(f'{len(list(db))}件登録しました。')
