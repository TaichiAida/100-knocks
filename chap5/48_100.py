# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
# ただし，構文木上のパスは以下の仕様を満たすものとする．
# 各文節は（表層形の）形態素列で表現する
# パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
import re

class Morph:
    def __init__(self,surface,bace,pos,pos1):
        self.surface = surface
        self.bace = bace
        self.pos = pos
        self.pos1 = pos1
    # それぞれの要素を返すメソッド（関数）
    def __str__(self):
        return "surface[{}] bace[{}] pos[{}] pos1[{}]".format(self.surface,self.bace,self.pos,self.pos1)

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.srcs = None

    def __str__(self):
        surface = ""
        for morph in self.morphs:
            surface += morph.surface
        return "{} dst[{}] srcs[{}]".format(surface,self.dst,self.srcs)

    def sentence_surface(self):
        surface = ""
        for morph in self.morphs:
            if morph.pos != "記号":
                surface += morph.surface
        return surface

    def sentence_pos(self,pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

def chunk_list():
    ans = []
    mid = []
    chunk = Chunk()

    with open("neko.txt.cabocha") as data:
        lines = data.readlines()
        for line in lines:
            if line[:3] == "EOS":
                
                if len(chunk.morphs) > 0:
                    mid.append(chunk)
                    chunk = Chunk()
                
                if len(mid) > 0:
                    ans.append(mid)
                    mid = []
            else:
                if line[0] == "*":
                    if len(chunk.morphs) > 0:
                        mid.append(chunk)
                        chunk = Chunk()
                    parts = line.split(" ")
                    parts[2] = int(re.sub("D","",parts[2]))
                    chunk.dst = parts[2]
                    chunk.srcs = parts[1]
                else:
                    words = line.split("\t")
                    parts = words[1].split(",")
                    morph = Morph(words[0],parts[6],parts[0],parts[1])
                    chunk.morphs.append(morph)
        return ans

if __name__ == "__main__":
    answers = chunk_list()
    for chunks in answers:
        for chunk in chunks:
            if chunk.sentence_pos("名詞"):
                word = chunk
                while word.dst != -1:
                    src = word.sentence_surface()
                    word = chunks[word.dst]
                    if src != "":
                        print(f"{src}->",end = "")
                end = word.sentence_surface()
                if end != chunk.sentence_surface():
                    print(end)
