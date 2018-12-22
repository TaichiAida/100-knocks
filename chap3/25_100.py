# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
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

################################
### {{基礎情報 ~ }} までを取り出す##
################################

#text = re.sub("<br/>","",text)
#text = re.sub("<ref>","",text)

# 正規表現の条件設定
pattern1 = re.compile(r"""
    ^\{\{基礎情報(.*)$  # 「基礎情報」のところから始める
    (.*)    # 任意の行
    ^\}\}$  # 終わりの行
    """,re.MULTILINE + re.VERBOSE + re.DOTALL)

# info:「基本情報」のデータが入っている
info = re.findall(pattern1,text)

# info は tuple型 となっており、全て info[0] に入っている
# print(type(info[0]))


######################
### | ~ \s を取り出す###
######################

# 正規表現の条件設定
pattern2 = re.compile(r"""
    \|([^(\s = \s)]+)    # 「|(フィールド名)」を取り出す。
    \s+
    =
    \s+                  # 「|(フィールド名) = (値)」
    (.+?)                # 任意の行
    (?:                  # キャプチャ対象外のグループ開始
        (?=\\n\|)        # 改行+'|'の手前
        | (?=$)          # または、終端の手前
    )                    # グループ終了
    """,re.MULTILINE + re.VERBOSE + re.DOTALL)

'''
print("「基本情報」抽出後")
print(str(info[0]))
print()
'''

info = re.findall(pattern2,str(info[0]))

'''
print("フィールドと値の抽出後")
print()
print(info)
'''

#####################
### 辞書への取り込み ###
#####################

dic = {}    # 辞書型
keys = []    # 辞書のキー
for data in info:
    dic[data[0]] = data[1]
    keys.append(data[0])

# 出力
for key in keys:
    print("{key}:{index}".format(key = key,index = dic[key]))

