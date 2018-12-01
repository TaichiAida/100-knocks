# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# ファイルの入力
data = "hightemp.txt"
count = 0

# 全ての内容を読み込む
# withを使うと close 忘れがない
with open(data) as datafile:
    # 読み込みは行ごと
    for line in datafile:
        count += 1

# 出力 
print (count)

# ターミナルから出力する
# $ chmod go+x （フォルダ名）chap2
# $ chmod +x （ファイル名）hightemp.txt
# $ chmod a+x （ファイル名）hightemp.txt
# $ wc -l （ファイル名）hightemp.txt