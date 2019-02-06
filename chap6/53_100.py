# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
# また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

# ダウンロードは済んでいる。あとはJava？
import xml.etree.ElementTree as ET
import json
import pprint
import corenlp

#  java -cp "/usr/local/lib/stanford-corenlp-full-2013-06-20/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP
# -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt

# 2013以前でないとcorenlpは使えない
#corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2018-10-05/"
"""
練習

corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2013-06-20/"

parser = corenlp.StanfordCoreNLP(corenlp_path = corenlp_dir)

result_json = json.loads(parser.parse("I am Alice."))
pprint.pprint(result_json)
"""
# 読み込み
tree = ET.parse("nlp.txt.xml")
for word in tree.iter("word"):
    print(f"{word.text}")
