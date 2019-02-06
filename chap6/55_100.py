# coding: utf-8

# 入力文中の人名をすべて抜き出せ．

import xml.etree.ElementTree as ET

# 読み込み
tree = ET.parse("nlp.txt.xml")

for word,pos,ner in zip(tree.iter("word"),tree.iter("POS"),tree.iter("NER")):
    #if pos.text == "NNP" and ner.text == "PERSON":
    if ner.text == "PERSON":
        print(f"{word.text}")
