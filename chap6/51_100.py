# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

import re

# 50
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

# 51
def split_words(list_):
    # 1行1単語の形式に変換する
    for line in list_:
        words = line.split(" ")
        for word in words:
            # right strip:右端の指定文字を削除した文字列を返す
            # この他にlstrip(left strip):左端
            yield word.rstrip(".,;:?!")

        # 終端では空行
        yield ""

##############################
# main

text = "nlp.txt"
answers = separate_re(text)
answers = split_words(answers)
for ans in answers:
    print(ans)
##############################
