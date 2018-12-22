# 記事から参照されているメディアファイルをすべて抜き出せ．
import gzip
import json
# 正規表現のために必要
import re

# イギリスに関する記事を返す関数
def searchText_UK():
    with gzip.open("jawiki-country.json.gz") as f:
        for line in f:
            obj = json.loads(line)
            if obj[u"title"] == u"イギリス":
                return obj["text"]

text = searchText_UK()
# print (text)


# answers = re.findall(r"\[\[Category:([^\]]+)\]\]", text)
answers = re.findall(r"(ファイル:|File:)([^\|]+)\|",text)

for answer in answers:
    # answer[0] = "ファイル　or　File"
    # answer[1] = "（ファイル名）"
    print(answer[1])
