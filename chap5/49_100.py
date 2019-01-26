import re
import copy

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

    # 指定した品詞の表層形を指定した文字に変える
    def surface_pos(self,pos,string):
        for morph in self.morphs:
            if morph.pos == pos:
                morph.surface = string
    
def chunk_list():
    ans = []
    mid = []
    chunk = Chunk()

    with open("neko.txt.cabocha") as data:
    #with open("test.txt") as data:
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

# 文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
# ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
    # 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
    # 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
# また，係り受けパスの形状は，以下の2通りが考えられる．
    # 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
    # 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．

# answer
# 文の中で名詞ペアを総当たり
# Xは | Yで -> 始めて -> 人間という -> ものを | 見た
# Xは | Yという -> ものを | 見た
# Xは | Yを | 見た
# Xで -> 始めて -> Y
# Xで -> 始めて -> 人間という -> Y
# Xという -> Y
if __name__ == "__main__":
    answers = chunk_list()
    for chunks in answers:
        # 名詞節が2つ以上あるかチェック
        noun_list = []
        for chunk in chunks:
            if chunk.sentence_pos("名詞"):
                noun_list.append(chunk)
        if len(noun_list) >= 2:
            ##########################
            # リストをコピーするときの注意
            ##########################
            # そのままコピーすると、片方の値を変えるともう片方も一緒に変わる
            # スライスを使うか、copyモジュールをインポートする
            noun_list_X = noun_list[:]
            noun_list_Y = noun_list[:]
            # 2つのリストを扱う。1つは末尾だけを抜き、もう1つは先頭から少しずつ抜く。
            noun_list_X.pop(-1)

            for noun_X in noun_list_X:
                # noun_Xと同じものを削除。同じ文節で行うのを回避
                noun_list_Y.remove(noun_X)
                # 全ての名詞ペアに対して検証する
                for noun_Y in noun_list_Y:

                    # 開始地点の表層形を記録
                    start_X = noun_X.sentence_surface()
                    start_Y = noun_Y.sentence_surface()

                    # 途中経過を記録する配列
                    mid_X = []
                    mid_Y = []

                    # XとYのかかる終端を探す
                    # word:変数扱い。Chunk型
                    word_X = copy.deepcopy(noun_X)
                    word_Y = copy.deepcopy(noun_Y)
                    #print(f"word_X:{word_X},word_Y:{word_Y}")

                    while word_X.dst != -1:
                        # 現在
                        src_X = word_X.sentence_surface()
                        # 1つ先
                        word_X = copy.deepcopy(chunks[word_X.dst])
                        #print(f"src_X:{src_X},word_X:{word_X}")

                        # 途中経過の記録
                        if src_X != start_X:
                            mid_X.append(src_X)
                        #print(f"mid_X:{mid_X}")

                        # 1つ先がYと一致したら終了
                        if word_X.sentence_surface() == start_Y:
                            #print("break")
                            break
                    
                    end_X = word_X.sentence_surface()

                    if end_X == start_Y:
                        # X->Yになる
                        # 出力前に名詞をXやYに変える
                        start_X = copy.deepcopy(noun_X)
                        start_X.surface_pos("名詞","X")
                        start_X = start_X.sentence_surface()

                        word_X.surface_pos("名詞"," Y")
                        end_X = word_X.sentence_surface()

                        # 出力処理
                        print(f"{start_X} -> ",end = "")
                        for x in mid_X:
                            print(f"{x} -> ",end = "")
                        print(end_X)
                        #print()
                    
                    else:
                        # X->Yにならない
                        while word_Y.dst != -1:
                            # 現在
                            src_Y = word_Y.sentence_surface()

                            # Yの途中経過がXの途中経過と被るかどうか
                            if src_Y in mid_X:
                                #end_Y = src_Y
                                #print("break")
                                #print(src_Y)
                                break
                            elif src_Y != start_Y:
                                mid_Y.append(src_Y)
                            
                            # 1つ先
                            word_Y = chunks[word_Y.dst]
                        # X|Y|(共通のかかり先)になる
                        # 出力前に先頭の名詞をX、Yに変える
                        
                        start_X = copy.deepcopy(noun_X)
                        start_X.surface_pos("名詞","X")
                        start_X = start_X.sentence_surface()

                        start_Y = copy.deepcopy(noun_Y)
                        start_Y.surface_pos("名詞","Y")
                        start_Y = start_Y.sentence_surface()

                        end_Y = word_Y.sentence_surface()

                        # 出力処理
                        print(f"{start_X} ",end = "")
                        if len(mid_X) > 0:
                            #print(" -> ",end = "")
                            for x in mid_X:
                                if x == end_Y:
                                    break
                                print("->",end = "")
                                print(f" {x} ",end = "")
                                #print(f"{x} -> ",end = "")
                        print("|",end = "")

                        print(f" {start_Y} ",end = "")
                        if len(mid_Y) > 0:
                            #print(" -> ",end = "")
                            for y in mid_Y:
                                print("->",end = "")
                                print(f" {y} ",end = "")
                                #print(f"{y} -> ",end = "")
                        print("|",end = "")

                        print(f" {end_Y}")
                    
                    # 毎回削除する
                    del word_X
                    del word_Y
        print()
                    