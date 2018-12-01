# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

# ファイルを読み込む
with open("hightemp.txt") as data:
    line = data.readlines()
    # index
    i = 0
    j = 0
    # dictionary
    dic = []
    index = []
    while i < len(line):
        word = line[i].split("\t")
        # print(int(word[2]))
        # 出力 41(int)
        dic.append(float(word[2]))
        index.append(int(i))
        i += 1
    print (dic,index)
    '''
    # 降順に並びかえ
    a = sorted(dic,reverse = True)
    print (a)
    '''
    # 昇順並び替え
    i = 0
    while i < len(line):
        j = i
        while j < len(line):
            if j == i:
                j += 1
                continue
            elif dic[j] < dic[i]:
                # 入れ替え
                dic[i],dic[j] = dic[j],dic[i]
                index[i],index[j] = index[j],index[i]
            j += 1
        i += 1
    
    print(dic,index)
    
    for x in index:
        print(line[x],end = "")
    print()

# ターミナルで実行
# $ sort hightemp.txt --key=3,3 --numeric-sort --reverse > result_test.txt
# $ sort (操作ファイル名) -k (操作したい列),(操作したい列) (複数列挙可能） -n(数値にする) -r(降順) > (出力先)
