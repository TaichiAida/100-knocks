# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
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
answers = re.findall(r"==+[^=]+==+",text)

for answer in answers:
    level = answer.count("=")
    # 割り算をすると　float型　になってしまうため、無理やり　int型 にする。
    level = int((level - 2) / 2)
    #print(level)
    #print(type(level))
    answer = re.sub("=","",answer)
    print("{indent}{section}({index})".format(indent = "\t"*(level-1),section = answer,index = level))
