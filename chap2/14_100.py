# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

n = int(input("N = "))

with open("hightemp.txt") as data:
    # index
    i = 0
    for line in data:
        print(line,end = "")
        i += 1
        if i == n:
            break

# ターミナルで確認
# $ cat hightemp.txt | head -n (N) > result_14.txt
