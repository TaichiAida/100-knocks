# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
# を与え，その実行結果を確認せよ．

import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
moji = []
moji = s.split()
print ("空欄区切り後は " + str(moji))
# index
i = 0
while i < len(moji):
    if len(moji[i]) <= 4:
        print (moji[i],end = ' ')
    else:
        # 先頭と末尾以外ランダムに並び替え
        tango = moji[i]
        change = tango[1:len(moji[i])-1]
        # print ("先頭と末尾を抜いた文字列は " + str(change))
        # リストに１文字ずつ入れる必要がある
        after = []
        for x in range(0,len(change)):
            after.append(change[x])
        random.shuffle(after)
        # リスト内の文字を繋げて出力したい
        # print ("シャッフル後は " + str(after))
        # リスト内の文字をひとまとめにする　join 反対はsplit
        result = ''.join(after)
        # print ("結合後は " + str(result))
        # 答え
        print (tango[0] + result + tango[-1],end = ' ')
    i = i + 1

