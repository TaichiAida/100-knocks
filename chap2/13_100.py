# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

# 結合したファイルを "col3.txt" に書き込む
with open("col1.txt") as col1, \
    open("col2.txt") as col2, \
    open("col3.txt",mode = "w") as col3:

    # 複数から取り出す時は zip() を使ってひとまとめにする
    for word1,word2 in zip(col1,col2):
        # col1 の各行の改行 \n を消さないと
        word1 = word1.split("\n")
        col3.write(word1[0] + "\t" + word2)

# ターミナルで実行
# $paste col1.txt col2.txt > result_13.txt
