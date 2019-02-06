# coding: utf-8
#  (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

##############################
# 力技

# 終端記号
def separate_power(text):
    last = [". ", "; ", ": ", "! ", "? "]
    cap = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    with open(text) as data:
        lines = data.readlines()
        ans = []
        for line in lines:
            # 先頭だけが出力された
            #print(line[0])
            i = 0 # index
            mid = ""
            if line[0] == "\n":
                continue
            while i < len(line):
                if line[i] != "\n":
                    mid += line[i]
                    #print(line[i],end = "")
                if i+2 < len(line):
                    if line[i]+line[i+1] in last:
                        if line[i+2] in cap:
                            #print(mid)
                            ans.append(mid)
                            mid = ""
                            #print()
                            i += 1 # 空白をスキップ
                i += 1
            if len(mid) > 0:
                #print(mid)
                ans.append(mid)
    return ans
##############################


# 正規表現が使えるのでは？
import re

##############################
# 正規表現
def separate_re(text):

    pattern_last = re.compile(r"""
        [\.|;|:|!|\?]   # 終端記号
        \s              # 空白
        [A-Z]           # A~Z
        """,re.VERBOSE) # VERBOSE：コメントっぽく書ける

    # 1行で書くとこう
    #pattern_last = re.compile(r"""[\.|;|:|!|\?]\s[A-Z]""")

    with open(text) as data:
        lines = data.readlines()
        ans = []
        for line in lines:
            i = 0
            mid = ""
            if line[0] == "\n":
                continue
            while i < len(line):
                if line[i] != "\n":
                    mid += line[i]
                if i+2 < len(line):
                    match = re.match(pattern_last,line[i]+line[i+1]+line[i+2])
                    if match:
                        ans.append(mid)
                        mid = ""
                        i += 1
                i += 1
            if len(mid) > 0:
                ans.append(mid)
    return ans

##############################


##############################
# main

text = "nlp.txt"
answers = separate_re(text)
for ans in answers:
    print(ans)
##############################
