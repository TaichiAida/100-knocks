# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

n = int(input("N = "))

with open("hightemp.txt") as data:
    line = data.readlines()
    # lineをn分割する
    split = len(line) / n
    # n分割した後
    i = 0
    while i < len(line):
        goal = i + split
        while i < goal:
            print (line[i],end = "")
            i += 1
        print()

# ターミナルで確認
# split -l (区切りたい行数) (ファイル名)