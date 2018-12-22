# 動詞の原形を全て抽出せよ.

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

# "pos":"動詞" の "bace": を抜き出す
answer = []
neko_txt = knock30()
for sentence in neko_txt:
    for word in sentence:
        if word["pos"] == "動詞":
            answer.append(word["bace"])
print(answer)
