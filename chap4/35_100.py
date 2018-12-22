# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

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

# "pos":"名詞"をできる限り繋げる
answer = []
neko_txt = knock30()
for sentence in neko_txt:
    i = 0
    while i < len(sentence):
        word1 = sentence[i]
        if word1["pos"] == "名詞":
            noun_phrase = word1["surface"]
            j = i + 1
            while j < len(sentence):
                words = sentence[j]
                if words["pos"] == "名詞":
                    noun_phrase += words["surface"]
                    j += 1
                # １度でも名詞発見に成功している場合、 answer に格納
                elif j > i + 1:
                    answer.append(noun_phrase)
                    break
                # １回目で失敗した場合、何もせず終了
                else:
                    break
        i += 1

print(answer)
