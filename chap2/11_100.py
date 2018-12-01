# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

# ファイルの入力
text = "hightemp.txt"

with open(text) as text_line:
    for line in text_line:
        # １行ずつ取り出す
        
        words = line
        # タブは \t という
        words = words.replace("\t"," ")
        print (words,end = "")
        print()

# ターミナルから出力
# "s/変換対象/変換する文字/g(当てはまるもの全て置換)" ファイル名
# $sed -e "s/\t/ /g" hightemp.txt
