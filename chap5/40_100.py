# 形態素を表すクラスMorphを実装せよ．
# このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
# さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

class Morph:
    def __init__(self,surface,bace,pos,pos1):
        self.surface = surface
        self.bace = bace
        self.pos = pos
        self.pos1 = pos1
    # それぞれの要素を返すメソッド（関数）
    def returnstr(self):
        return "surface[{}] bace[{}] pos[{}] pos1[{}]".format(self.surface,self.bace,self.pos,self.pos1)

ans = []
mid = []

with open("neko.txt.cabocha") as data:
    lines = data.readlines()
    for line in lines:
        # EOS ~ EOSまでで１文
        if line[:3] == "EOS":
            if len(mid) > 0:
                ans.append(mid)
                mid = []
        else:
            # *（数字）を除く
            if line[0] == "*":
                continue
            else:
                # words[0]:表層形,words[1]:形態素解析結果
                words = line.split("\t")
                # parts[6]:基本形,[0]:品詞,[1]:品詞細分類1
                parts = words[1].split(",")
                # morph:Class Morph
                morph = Morph(words[0],parts[6],parts[0],parts[1])
                mid.append(morph.returnstr())

for x in ans[3]:
    print(x)
