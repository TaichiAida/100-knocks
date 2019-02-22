# coding utf-8

# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

from graphviz import Digraph
import xml.etree.ElementTree as ET

# 読み込み
tree = ET.parse("nlp.txt.xml")
G = Digraph(format="png")
G.attr("node", shape="square", style="filled")
#sentence = tree.findall("./document/sentences/")[0]
sentences = tree.findall("./document/sentences/")
for sentence in sentences:
    collapsed = sentence.findall("./dependencies[@type='collapsed-dependencies']/")

    # グラフ化
    for collapse in collapsed:
        start = collapse.findtext("governor")
        end = collapse.findtext("dependent")
        #print(start,end)
        G.edge(start,end)

G.render("graphs")