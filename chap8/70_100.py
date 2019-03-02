# coding utf-8

# 以下の要領で正解データ（sentiment.txt）を作成せよ
# 1. rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# 2. rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 3. 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

import glob
import random

# pos labeled list
labeled_pos = []

# neg labeled list
labeled_neg = []

# pos and neg labeled list
labeled_result = []

# デコードでエラー。そのままだと"utf-8"でデコードできない文字コードがあるらしい。
# encoding = "cp1252" で解決
# positive
with open("rt-polaritydata/rt-polaritydata/rt-polarity.pos",mode="r",encoding="cp1252") as p:
    lines = p.readlines()
    for line in lines:
        #print(line)
        labeled_line = "+1" + " " + line
        # リストに要素を追加する場合はappend
        labeled_pos.append(labeled_line)
        #print(labeled_line)
    #print(len(labeled_pos))

# negative
with open("rt-polaritydata/rt-polaritydata/rt-polarity.neg",mode="r",encoding="cp1252") as n:
    lines = n.readlines()
    for line in lines:
        #print(line)
        labeled_line = "-1" + " " + line
        # リストに要素を追加する場合はappend
        labeled_neg.append(labeled_line)
        #print(labeled_line)
    #print(len(labeled_neg))

# リストにリストを追加するが、要素だけを追加したい場合はappendではなくextend
labeled_result.extend(labeled_pos)
labeled_result.extend(labeled_neg)
#print(labeled_result)

# 要素をランダムに並び替える
random.shuffle(labeled_result)
for result in labeled_result:
    print(result,end="")
    
# pos 5331 sentences
# neg 5331 sentences