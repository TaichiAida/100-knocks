# Chunkのリストとして表現したい
import re

# 40のプログラム
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
    # 40に加えて，文節を表すクラスChunkを実装せよ．
    # このクラスは形態素（Morphオブジェクト）のリスト（morphs），
    # 係り先文節インデックス番号（dst），
    # 係り元文節インデックス番号のリスト（srcs）
    # をメンバ変数に持つこととする．
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.srcs = None
    def __str__(self):
        surface = ""
        for morph in self.morphs:
            surface += morph.surface
        return "{} dst[{}] srcs[{}]".format(surface,self.dst,self.srcs)

def chunk_list():
    # さらに，入力テキストのCaboChaの解析結果を読み込み，
    # １文をChunkオブジェクトのリストとして表現し，
    # 8文目の文節の文字列と係り先を表示せよ．
    ans = []
    mid = []
    chunk = Chunk()

    with open("neko.txt.cabocha") as data:
        lines = data.readlines()
        # EOS ~ EOSまでで１文
        for line in lines:
            if line[:3] == "EOS":
                
                if len(chunk.morphs) > 0:
                    #mid.append(chunk.__str__())
                    mid.append(chunk)
                    chunk = Chunk()
                
                if len(mid) > 0:
                    ans.append(mid)
                    mid = []
            else:
                if line[0] == "*":
                    if len(chunk.morphs) > 0:
                        #mid.append(chunk.__str__())
                        mid.append(chunk)
                        chunk = Chunk()
                    # parts[2]:dst,[1]srcs
                    parts = line.split(" ")
                    parts[2] = int(re.sub("D","",parts[2]))
                    chunk.dst = parts[2]
                    chunk.srcs = parts[1]
                else:
                    # words[0]:表層形,words[1]:形態素解析結果
                    words = line.split("\t")
                    # parts[6]:基本形,[0]:品詞,[1]:品詞細分類1
                    parts = words[1].split(",")
                    # morph:Class Morph
                    morph = Morph(words[0],parts[6],parts[0],parts[1])
                    chunk.morphs.append(morph)
        return ans

if __name__ == "__main__":
    ans = chunk_list()
    for i,answer in enumerate(ans[5]):
        print(f"{i} {answer}")
