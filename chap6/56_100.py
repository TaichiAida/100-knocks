# coding utf-8

# Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
# ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

import xml.etree.ElementTree as ET

# 読み込み
tree = ET.parse("nlp.txt.xml")

for word in tree.iter("word"):
    print(f"{word.text}")