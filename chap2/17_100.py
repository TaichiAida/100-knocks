# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

# 1列目を読み込む
with open("hightemp.txt") as data:
    line = data.readlines()

    # index
    i = 0
    # 異なる文字列の集合のリスト
    answer = []

    while i < len(line): 
        # 行をタブ区切りでsplit
        word = line[i].split("\t")

        # print(word[0])
        # 出力　高知県

        if not word[0] in answer:
            answer.append(word[0])
        
        i += 1

    print(answer)

# ターミナルで実行
# cut -f 1(文字数,タブ区切り) hightemp.txt | sort | uniq > result.txt