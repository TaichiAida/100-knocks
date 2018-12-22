# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
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
#print (text)
answers = re.findall(r"\[\[Category:([^\]]+)\]\]", text)
for answer in answers:
    print(answer)

"""
answer
イギリス|*
英連邦王国|*
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国|くれいとふりてん
1801年に設立された州・地域
"""