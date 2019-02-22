# coding utf-8

# Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．
# ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

import xml.etree.ElementTree as ET

# 読み込み
tree = ET.parse("nlp.txt.xml")

# menrion representative = "true"ごとにまとめる？
rep_dict = {}
num = 1
for coreference in tree.findall("./document/coreference/coreference"):
#coreference = tree.findall("./document/coreference/coreference")[0]

    # 代表参照表現の取得

    # text_idの取得
    text_id = {}
    sentence_id = coreference.findall('./mention[@representative="true"]/')[0].text
    start_id = coreference.findall('./mention[@representative="true"]/')[1].text
    end_id = coreference.findall('./mention[@representative="true"]/')[2].text

    # textの取得
    sentences = tree.findall("./document/sentences/")
    for sentence in sentences:
        if sentence.get("id") == sentence_id:
            tokens = sentence.findall("./tokens/")
            break

    rep_text = ""
    i = 1
    flag = False
    for token in tokens:
        if i == int(start_id):
            word = token.findall("word")[0]
            rep_text += word.text + " "
            flag = True
        elif i == int(end_id)-1:
            word = token.findall("word")[0]
            rep_text += word.text
            flag = False
        elif flag:
            word = token.findall("word")[0]
            rep_text += word.text + " "
        i += 1
    print(f"{num}\t{rep_text}")
    num += 1

    # 置き換え対象の取得
    for mention in coreference.findall('./mention'):
        # 代表参照表現のidを除く
        if sentence_id != mention.findtext("sentence") and start_id != mention.findtext("start") and end_id != mention.findtext("end"):
            rep_dict[mention.findtext("sentence"),mention.findtext("start")] = (mention.findtext("end"),rep_text)
        
print(rep_dict)


# 本文を置き換えながら出力
for sentence in sentences:
#sentence = sentences[0]
    sentence_id = sentence.get("id")
    tokens = sentence.findall("./tokens/")
    for token in tokens:
        token_id = token.get("id")
        if (sentence_id,token_id) in rep_dict:
            (end_id,rep_text) = rep_dict[(sentence_id,token_id)]
            print("「",end="")

        print(token.findtext("word"),end=" ")

        if token_id == end_id:
            print(f"({rep_text})」",end=" ")
    print()
