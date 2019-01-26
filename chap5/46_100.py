# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
# 45の仕様に加えて，以下の仕様を満たすようにせよ．
# 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

import re

class Morph:
    def __init__(self,surface,bace,pos,pos1):
        self.surface = surface
        self.bace = bace
        self.pos = pos
        self.pos1 = pos1

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
    
    # srcの助詞をlistで返す
    def sentence_particle(self):
        surface = []
        for morph in self.morphs:
            if morph.pos == "助詞":
                surface.append(morph.surface)
        surface.sort()
        return surface
    
    # dstの最左動詞の基本形（bace）を返す
    def sentence_bace(self):
        for morph in self.morphs:
            if morph.pos == "動詞":
                return morph.bace

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
        #return ans[3]

# 重複の削除＋空白区切で並べる関数
def UniqAndSpace(dic,keys):
    for key in keys:
        key = str(key)
        dic[key] = list(set(dic[key]))
        dic[key].sort()
        dic[key] = " ".join(dic[key])

if __name__ == "__main__":
    # chunk_lists:[文、文、文、文、文…]
    chunk_lists = chunk_list()
    ans_list1 = []
    ans_list2 = []
    ans_key = []
    # chunks:[文節、文節、文節、文節、文節…]
    for chunks in chunk_lists:
        particle_dic = {}
        kou_dic = {}
        dst_key = []
        # chunk:文節
        for chunk in chunks:
            if chunk.dst != -1:
                src_chunk = chunk
                dst_chunk = chunks[chunk.dst]

                #if src_chunk.sentence_pos("名詞") and dst_chunk.sentence_pos("動詞"):
                if dst_chunk.sentence_pos("動詞"):
                    src = src_chunk.sentence_surface()
                    dst = dst_chunk.sentence_surface()
                    if src != "" and dst != "":
                        # ここまでが43の内容
                        ####################################

                        ####################################
                        # ここから45の内容
                        # 文(chunks)内で別の文節が同じ文節にかかった場合
                        # ex.8文目) chunks[0].dst = chunks[4].dst
                        # chunks内で共通の辞書を定義
                        # 助詞を入れておく
                        
                        # srcから助詞を抜き出す
                        src_particle_list = chunk.sentence_particle()
                        if len(src_particle_list) > 0:
                            # dstを最左動詞の原形に直す
                            dst_bace = dst_chunk.sentence_bace()
                            
                            #####################
                            # 辞書への追加
                            
                            # 辞書にdstのキーに対応する値がない場合（キーのリストを検索する）
                            # 辞書、キーのリストに新規で作成
                            if dst_bace not in dst_key:
                                dst_key.append(dst_bace)
                                particle_dic[dst_bace] = []
                                kou_dic[dst_bace] = []
                            # 辞書のリストに追加
                            for src_particle in src_particle_list:
                                particle_dic[dst_bace].append(src_particle)
                            kou_dic[dst_bace].append(src)
                            #####################
        # 各辞書内の処理
        # 重複の削除＋空白区切で並べる
        for key in dst_key:
            key = str(key)
            particle_dic[key] = list(set(particle_dic[key]))
            particle_dic[key].sort()
            particle_dic[key] = " ".join(particle_dic[key])
        UniqAndSpace(kou_dic,dst_key)

        # 解答の辞書、キーのリストに１文の結果を追加
        ans_list1.append(particle_dic)
        ans_list2.append(kou_dic)
        ans_key.append(dst_key)
        
    for dic1,dic2,keys in zip(ans_list1,ans_list2,ans_key):
        for key in keys:
            print(f"{key}\t{dic1[key]}\t{dic2[key]}")
