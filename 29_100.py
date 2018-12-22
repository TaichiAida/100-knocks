# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
import gzip
import json
# 正規表現のために必要
import re

import requests

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

info = re.findall(pattern2,str(info[0]))

#####################
### 辞書への取り込み ###
#####################

dic = {}    # 辞書型
keys = []    # 辞書のキー
for data in info:
    dic[data[0]] = data[1]
    keys.append(data[0])


#######################
### 国旗画像URLの取得 ###
#######################

flag = dic["国旗画像"]
url = 'https://en.wikipedia.org/w/api.php?'
payload = {
        'action': 'query',
        'format': 'json',
        'titles': f'File: flag',
        'prop': 'imageinfo',
        'iiprop': 'url'
}
r = requests.get(url, params=payload).text  # 文字列に変換

print("{}".format(re.findall(r'"url":"(.*?)"', r)))
