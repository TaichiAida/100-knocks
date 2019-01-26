# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
# 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．

# ただし，出力は以下の仕様を満たすようにせよ．
# 動詞を含む文節において，最左の動詞の基本形を述語とする
# 述語に係る助詞を格とする
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

# このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
# コーパス中で頻出する述語と格パターンの組み合わせ
# 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）

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

if __name__ == "__main__":
    # chunk_lists:[文、文、文、文、文…]
    chunk_lists = chunk_list()
    ans_list = []
    ans_key = []
    # chunks:[文節、文節、文節、文節、文節…]
    for chunks in chunk_lists:
        particle_dic = {}
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
                            # 辞書のリストに追加
                            for src_particle in src_particle_list:
                                particle_dic[dst_bace].append(src_particle)
                            #####################
        # 各辞書内の処理
        # 重複の削除＋空白区切で並べる
        for key in dst_key:
            key = str(key)
            particle_dic[key] = list(set(particle_dic[key]))
            particle_dic[key].sort()
            particle_dic[key] = " ".join(particle_dic[key])

        # 解答の辞書、キーのリストに１文の結果を追加
        ans_list.append(particle_dic)
        ans_key.append(dst_key)
        
    for dic,keys in zip(ans_list,ans_key):
        for key in keys:
            print(f"{key}\t{dic[key]}")
    
# UNIXコマンド
# grep 与える result45.txt | sort | uniq -c | sort -r  > result45_give.txt
# 「与える」のある列の抜き出し | 並び換え | 重複をカウントして削除 | 降順並び替え > hoge.txt
# する、見るも同様