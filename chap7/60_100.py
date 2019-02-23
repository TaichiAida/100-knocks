# coding utf-8
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．

# KVS:LevelDB, Redis, KyotoCabinet, memchaed, Big Table

# dic["アーティスト名(name)"] = "活動場所(area)"
import json
import gzip

with gzip.open("artist.json.gz") as data:
    for d in data:
        obj = json.loads(d)
        #obj = json.loads(d)
        print(obj)         
        
