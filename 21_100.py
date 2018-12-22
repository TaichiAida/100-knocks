# 記事中でカテゴリ名を宣言している行を抽出せよ．
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
answers = re.findall(r"\[\[Category:[^\]]+\]\]", text)
for answer in answers:
    print(answer)

"""
answer
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""