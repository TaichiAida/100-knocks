# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．
# さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．

import gzip
import json
import plyvel

def makeDB():
    db = plyvel.DB("./db_tag_60/", create_if_missing=True)
    with gzip.open("artist.json.gz") as data:
        for line in data:
            dic = json.loads(line)
            if "name" in dic and "tags" in dic:
                # list型になっているものはそのままencodeできなかった
                # json.dumpsでエンコード
                # デコードするときはjson.loads
                db.put(dic["name"].encode("utf-8"),json.dumps(dic["tags"]).encode("utf-8"))
    # 確認用
    print(f"{len(list(db))}件登録しました")

def search_tags_from_artist(name):
    db = plyvel.DB("./db_tag_60",create_if_missing=True)
    try:
        #tags = db.get(name.encode("utf-8")).decode("utf-8")
        # デコードするときはjson.loads
        tags = json.loads(db.get(name.encode("utf-8")))
    except:
        tags = "登録されていません"
    db.close()
    return tags

if __name__ in "__main__":
    makeDB()
    while True:
        name = input("--artist name here--\n<end> means exit\n")
        if name == "end":
            print("--exit--")
            break
        else:
            tags = search_tags_from_artist(name)
            if tags != "登録されていません":
                for tag in tags:
                    print(tag)
            else:
                print(tags)
