# coding utf-8

# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
# 「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
# ただし，主語，述語，目的語の定義は以下を参考にせよ．
#   述語: nsubj関係とdobj関係の子（dependant）を持つ単語
#   主語: 述語からnsubj関係にある子（dependent）
#   目的語: 述語からdobj関係にある子（dependent）

import xml.etree.ElementTree as ET

# 読み込み
tree = ET.parse("nlp.txt.xml")

ans = []

##sentence = tree.findall("./document/sentences/")[2]
for sentence in tree.findall("./document/sentences/"):

   #print(len(tree.findall("./document/sentences"))) = 1
   #sentence id = 1 ~ 50
   #print(len(tree.findall("./document/sentences/"))) = 50
   collapsed = sentence.findall("./dependencies[@type='collapsed-dependencies']")

   # id = 3
   # understanding"\t"enabling"\t"computers
   # search nsubj and dobj

   #print(len(collapsed.findall("dep[@type='nsubj']")))
   #collapsed: number of types
   #print(len(collapsed)) = 23

   """
   #for types in zip(collapsed.findall("dep[@type='nsubj']"),collapsed.findall("dep[@type='dobj']")):
   for types in collapsed.findall("dep[@type='nsubj']"):
      v_idx = types.get("id")
      print(v_idx)

   """
   nsubj_list = []
   for collapse in collapsed:
      for types in collapse.findall("dep[@type='nsubj']"):
         ##for types in collapse.findall("dep[@type='nsubj']/governor"):
         v = types.findall("./governor")
         s = types.findall("./dependent")
         ##v_idx = types.get("idx")
         v_idx = v[0].get("idx")
         s_idx = s[0].get("idx")
         #print(f"v_idx:{v_idx}\ts_idx:{s_idx}")
         
         v_text = v[0].text
         s_text = s[0].text
         #print(f"v_text:{v_text}\ts_text:{s_text}")
         
         # 辞書に追加
         nsubj_dic = {
            "v_idx":v_idx,
            "v_text":v_text,
            "s_idx":s_idx,
            "s_text":s_text
         }
         nsubj_list.append(nsubj_dic)
         #print()
      # 何かに記録しておく？辞書のリストなど

      # この後 dobj で探す。v_idxが一致するかどうか
      for types in collapse.findall("dep[@type='dobj']"):
         v = types.findall("./governor")
         o = types.findall("./dependent")
         v_idx = v[0].get("idx")
         o_idx = o[0].get("idx")
         #print(f"v_idx:{v_idx}\to_idx:{o_idx}")
         
         v_text = v[0].text
         o_text = o[0].text
         #print(f"v_text:{v_text}\to_text:{o_text}")

         for nsubj in nsubj_list:
            if v_idx == nsubj["v_idx"]:
               #print("true")
               mid = {
                  "s":nsubj["s_text"],
                  "v":nsubj["v_text"],
                  "o":o_text
               }
               ans.append(mid)
         #print()
# 出力

for answers in ans:
   #print(type(answers))
   #print(answers)
   print(f"{answers['s']}\t{answers['v']}\t{answers['o']}")

# ""と''で分ける。