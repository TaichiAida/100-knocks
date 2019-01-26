# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
# 46のプログラムを以下の仕様を満たすように改変せよ．
# 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

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

    # サ変接続の名詞＋「を」(助詞)
    def SahenPlusWo(self):
        if len(self.morphs) == 2:
            if self.morphs[0].pos1 == "サ変接続" and self.morphs[1].pos == "助詞" and self.morphs[1].surface == "を":
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
    ans_ju = []
    # chunks:[文節、文節、文節、文節、文節…]
    for chunks in chunk_lists:
        particle_dic = {}
        kou_dic = {}
        ju_dic = {}
        dst_key = []
        # chunk:文節
        for chunk in chunks:
            if chunk.dst != -1:
                src_chunk = chunk
                dst_chunk = chunks[chunk.dst]
                dst_id = str(chunk.dst)
                # 動詞　かどうか
                if dst_chunk.sentence_pos("動詞"):
                    src = src_chunk.sentence_surface()
                    dst = dst_chunk.sentence_surface()
                    if src != "" and dst != "":
                        # dstを最左動詞の原形に直す
                        dst_bace = dst_chunk.sentence_bace()
                        # サ変＋を かどうか
                        if src_chunk.SahenPlusWo():
                            # 今回の述語＝サ変名詞＋を＋動詞の原形
                            jutugo = src + dst_bace
                            if dst_id not in dst_key:
                                dst_key.append(dst_id)
                                particle_dic[dst_id] = []
                                kou_dic[dst_id] = []
                            ju_dic[dst_id] = jutugo
                        else:
                            # srcから助詞を抜き出す
                            src_particle_list = chunk.sentence_particle()
                            if len(src_particle_list) > 0:
                                #####################
                                # 辞書への追加
                                # すでに辞書ができている or できていない　判別方法？
                                # 辞書にdstのキーに対応する値がない場合（キーのリストを検索する）
                                if dst_id not in dst_key:
                                    dst_key.append(dst_id)
                                    particle_dic[dst_id] = []
                                    kou_dic[dst_id] = []
                                
                                # 辞書のリストに追加
                                for src_particle in src_particle_list:
                                    particle_dic[dst_id].append(src_particle)
                                kou_dic[dst_id].append(src)
                                    #####################
        # dst_keyから述語になれなかったdstを削除
        for key in dst_key:
            if key not in ju_dic:
                dst_key.remove(key)
        UniqAndSpace(particle_dic,dst_key)
        UniqAndSpace(kou_dic,dst_key)
        # 解答の辞書、キーのリストに１文の結果を追加
        ans_list1.append(particle_dic)
        ans_list2.append(kou_dic)
        ans_key.append(dst_key)
        ans_ju.append(ju_dic)
        
    for dic1,dic2,keys,jutugos in zip(ans_list1,ans_list2,ans_key,ans_ju):
        for key in keys:
            if key in jutugos:
                print(f"{jutugos[key]}\t{dic1[key]}\t{dic2[key]}")