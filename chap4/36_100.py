# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

# 30のプログラム
def knock30():
    text = []
    interim = []
    with open("neko.txt.mecab") as data:
        lines = data.readlines()
        for line in lines:
            if line[0:3] == "EOS":
                if len(interim) > 0:
                    text.append(interim)
                    interim = []
            else:
                contents = line.split("\t")
                words = contents[1].split(",")
                dic = {}
                dic["surface"] = contents[0]
                dic["bace"] = words[6]
                dic["pos"] = words[0]
                dic["pos1"] = words[1]
                interim.append(dic)
    return text

# "surface":"単語名" が word_List に
# ある -> カウントを増やす
# ない -> 追加、カウントを１に
answer = []
word_List = {}
neko_txt = knock30()
for sentence in neko_txt:
    for word in sentence:
        if word["surface"] not in word_List:
            word_List[word["surface"]] = 1
        else:
            word_List[word["surface"]] += 1

# 得られた結果について、辞書型のvalueをsortする
# keyをsortするときは lambda x:x[0] と記述
answer = sorted(word_List.items(),key = lambda x:x[1],reverse = True)
print(answer)
