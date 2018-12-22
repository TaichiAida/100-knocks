# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

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

# "pos":"名詞"、"pos":"助詞"、"pos":"名詞"
# 3つの "surface": をまとめて抜き出す
answer = []
neko_txt = knock30()
for sentence in neko_txt:
    i = 0
    while i < len(sentence)-2:
        word1 = sentence[i]
        if word1["pos"] == "名詞":
            word2 = sentence[i+1]
            if word2["surface"] == "の" and word2["pos"] == "助詞" and word2["pos1"] == "連体化":
                word3 = sentence[i+2]
                if word3["pos"] == "名詞":
                    noun_phrase = word1["surface"] + word2["surface"] + word3["surface"]
                    answer.append(noun_phrase)
        i += 1

print(answer)
