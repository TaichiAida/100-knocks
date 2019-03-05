# coding utf-8
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
# 素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．

from stemming.porter2 import stem
import re
from collections import Counter

# Oracle text のストップワード
stop_words = (
    "a did in only then where "
    "all do into onto there whether "
    "almost does is or therefore which "
    "also either it our these while "
    "although for its ours they who "
    "an from just s this whose "
	"and had ll shall those why "
    "any has me she though will "
    "are have might should through with "
    "as having Mr since thus would "
    "at he Mrs so to yet "
    "be her Ms some too you "
    "because here my still until your "
    "been hers no such ve yours "
    "both him non t very "
    "but his nor than was "
    "by how not that we "
    "can however of the were "
    "could i on their what "
    "d if one them when").split(" ")

# ストップワードを検出する関数
def boolChecker(word):
    if word.lower() in stop_words:
        return True
    return False


# ここからメインの処理
# 素性の出現回数をカウントする辞書
feature_dic = Counter()
with open("sentiment.txt") as data:
    lines = data.readlines()
    for line in lines:
        line = line.split(" ")
        # "+1" "-1"はいらない
        for word in line[3:]:
            # 「ストップワードでない」かつ「記号でない」
            if not boolChecker(word) and len(word) > 1:
                if "\n" in word:
                    word = re.sub(r"\n","",word)
                # カウントする辞書に追加
                feature_dic.update([word])
# 出力
for feature,count in feature_dic.most_common(n=None):
    # 出現回数が5回以下のものは除去
    if count <= 5:
        break
    else:
        print(feature)