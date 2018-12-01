# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ

# ファイルへの書き込み
# ファイルを読み込む
data_file = "hightemp.txt"

# ファイルを複数開くときは ", \" で区切り、最後に ":" をつける
with open(data_file) as data, \
    open("col1.txt",mode = "w") as col1, \
    open("col2.txt",mode = "w") as col2:
    # forループで元のファイルを参照する
    for line in data:
        # タブで区切る
        col = line.split("\t")
        # 1列目をcol1、2列目をcol2に書き込む
        col1.write(col[0] + "\n")
        col2.write(col[1] + "\n")

# ターミナルで実行する
# $ cut -f 1  hightemp.txt > col1.txt
# $ cut -f 2  hightemp.txt > col2.txt