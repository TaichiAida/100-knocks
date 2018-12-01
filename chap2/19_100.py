# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

with open("hightemp.txt") as data:
    line = data.readlines()
    words = []
    i = 0
    while i < len(line):
        word = line[i].split("\t")
        words.append(word[0])
        i += 1
    # １行目が入力されていることを確認
    print(words)
    words.sort()
    print(words)
    # 並び替えた後、countで要素数を数える
    # i(index)+= value(count結果)
    # 文字、要素数で2つのリストを管理（18_100.pyと同様）
    j = 0
    index = []
    value = []
    while j < len(words):
        index.append(words.count(words[j]))
        value.append(words[j])
        j += words.count(words[j])
    print(value,index)
    
    # 降順並び替え
    i = 0
    while i < len(index):
        j = i
        while j < len(index):
            if j == i:
                j += 1
                continue
            elif index[j] > index[i]:
                # 入れ替え
                value[i],value[j] = value[j],value[i]
                index[i],index[j] = index[j],index[i]
            j += 1
        i += 1
    
    print(value,index)

    # ターミナルで実行
    # $ cut -f　1 hightemp.txt | sort | uniq -c | sort -r