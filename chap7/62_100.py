# coding utf-8
# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．

import plyvel

db = plyvel.DB("./db_60",create_if_missing=True)

count = 0
for data in db:
    #print(data[1]) # b'Japan'
    #print(type(data[1]))   # byte
    if data[1] == "Japan".encode("utf-8"):
        #print(data)
        count += 1
print(f"Japan:{count}人です")
