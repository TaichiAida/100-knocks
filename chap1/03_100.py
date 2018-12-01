# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ
moji = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# リストの初期化
result = []

# 単語で区切る
#print (moji.split())
#result.append(moji.split())
#print (result)  # 大きなリスト1つの中に分割されたリストが入っている

# 区切った文字一つ一つについて検討
words = moji.split()
for word in words:
    count = 0
    count = len(word)
    # ","と"."が含まれている
    count = count - word.count(",") - word.count(".")
    result.append(count)
print (result)
