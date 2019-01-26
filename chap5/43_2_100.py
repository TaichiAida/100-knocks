# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．
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
            if chunk.dst != -1:
                src_chunk = chunk
                dst_chunk = chunks[chunk.dst]

                if src_chunk.sentence_pos("名詞") and dst_chunk.sentence_pos("動詞"):
                    src = chunk.sentence_surface()
                    dst = chunks[chunk.dst].sentence_surface()
                    if src != ""and dst != "":
                        print(f"{src}\t{dst}")
