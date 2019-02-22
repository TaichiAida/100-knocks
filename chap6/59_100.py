# coding utf-8

# Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．
# 入れ子になっている名詞句もすべて表示すること．

import xml.etree.ElementTree as ET
import re


def getNP(parse):
    count = 0   # かっこのカウント
    parse = parse[0].text.split(" ")
    i = 0
    while i < len(parse):
        word = parse[i]
        if word == "(NP":
            count = 1
            #print(i)
            #print(word,end=" ")
            #for word in parse[i:]:
            j = i+1
            while j < len(parse):
                word = parse[j]
                if "(" in word:
                    count += int(word.count("("))
                    #print(word,end=" ")
                elif ")" in word:
                    count -= int(word.count(")"))
                    word = re.sub(r"\)","",word)
                    
                    # count == 0 を終了条件にすると、~ (NP (NN NLP)))) などに対処不可
                    if count < 0:
                        print(word)
                        break
                    else:
                        print(word,end=" ")
                j += 1
        i += 1


# 読み込み
tree = ET.parse("nlp.txt.xml")

#sentence = tree.findall("./document/sentences/")[2]
for sentence in tree.findall("./document/sentences/"):
    print(f"id:{sentence.get('id')}")
    parse = sentence.findall("./parse")
    getNP(parse)
    print()

#print(parse[0].text)
"""
flag = 0
count = 0   # かっこのカウント
for word in parse[0].text.split(" "):
    if flag == 1:
        #print(word,end=" ")
        if "(" in word:
            count += int(word.count("("))
            #print(count)
        elif ")" in word:
            count -= int(word.count(")"))
            #print(type(word))
            word = re.sub(r"\)","",str(word))
            print(word,end=" ")
            #print(count)
        if count == 0:
            flag = 0
            print()
    elif word == "(NP":
        flag = 1
        #print(word,end=" ")
        if count == 0:
            count = 1
            #print(count)
"""
"""
def getNP(parse):
    flag = 0
    count = 0   # かっこのカウント
    parse = parse[0].text.split(" ")
    i = 0
    while i < len(parse):
        word = parse[i]
        if word == "(NP":
            count = 1
            print(i)
            #print(word,end=" ")
            #for word in parse[i:]:
            j = i+1
            while j < len(parse):
                word = parse[j]
                if "(" in word:
                    count += int(word.count("("))
                    #print(word,end=" ")
                elif ")" in word:
                    count -= int(word.count(")"))
                    word = re.sub(r"\)","",word)
                    
                    # count == 0 を終了条件にすると、~ (NP (NN NLP)))) などに対処不可
                    if count < 0:
                        print(word)
                        break
                    else:
                        print(word,end=" ")
                j += 1
        i += 1
"""