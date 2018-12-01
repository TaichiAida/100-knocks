# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

n = int(input("N = "))

with open("hightemp.txt") as data:
    # index
    i = 0
    '''
    print (type(data))
    print (type(2))
    # print (data[0]) list型ではないため、インデックスは使えない
    # data = data.reverse()
    '''
    # list型になる
    lines = data.readlines()
    print (type(lines))
    # 先頭
    print (lines[0],end = "")
    # 末尾
    print (lines[-1],end = "")
    '''
    for line in data:
        print(line,end = "")
        i += 1
        if i == n:
            break
    '''
    print ("出力結果はここから")
    while i < n:
        print (lines[-1-i],end = "")
        i += 1
        # 暴走防止
        if i+1 > len(lines):
            break
    
    # 出力方法についてもういちど考える
    # print (lines[len(lines)-n:-1])

# ターミナルで確認
# $ cat hightemp.txt | tail -n (N) > result_15.txt
