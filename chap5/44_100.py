# 与えられた文の係り受け木を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

from graphviz import Digraph

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

def chunk_list():
    ans = []
    mid = []
    chunk = Chunk()
    print("出力したいのは第何文目？")
    num = int(input())
    # 文の数は9210。範囲外の場合以下の処理を行う。
    if num > 9210:
        num %= 9210
    elif num < 0:
        num *= -1
        num %= 9210
    
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
        return ans[num]

if __name__ == "__main__":
    chunks = chunk_list()

    G = Digraph(format="png")
    G.attr("node", shape="square", style="filled")

    for chunk in chunks:
        if chunk.dst != -1:
            src = chunk.sentence_surface()
            dst = chunks[chunk.dst].sentence_surface()
            if src != ""and dst != "":
                G.edge(src,dst)

    G.render("graphs")

