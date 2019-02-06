# Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
import xml.etree.ElementTree as ET
# 読み込み
tree = ET.parse("nlp.txt.xml")

for word,lemma,pos in zip(tree.iter("word"),tree.iter("lemma"),tree.iter("POS")):
    print(f"{word.text}\t{lemma.text}\t{pos.text}")
