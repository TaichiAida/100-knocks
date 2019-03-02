# coding utf-8
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
# さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
# さらに，その関数に対するテストを記述せよ．

# Oracle text のストップワード
"""
これだとエラー。長いstrは
(
    "長い文章"
    "ダブルクオーテーションで区切る"
)
出力："長い文章ダブルクオーテーションで区切る" 
ダブルクオーテーション同士はそのまま連結

stop_words = (
    "a did in only then where",
    "all do into onto there	whether",
    "almost does is therefore which",
    "also either it our these while",
    "although for its ours they who",
    "an from just s this whose",
	"had ll shall those why",
    "any has me she though will",
    "are have might should through with",
    "as having Mr since thus would",
    "at he Mrs so to yet",
    "be her Ms some too you",
    "because here my still until your",
    "been hers no such ve yours",
    "both him non t very",
    "but his nor than was",
    "by how not that we",
    "can however of the were",
    "could i on their what",
    "d if one them when").split(" ")
"""

stop_words = (
    "a did in only then where "
    "all do into onto there whether "
    "almost does is therefore which "
    "also either it our these while "
    "although for its ours they who "
    "an from just s this whose "
	"had ll shall those why "
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
#print(stop_words)

def boolChecker(word):
    if word.lower() in stop_words:
        return True
    return False

# テストするにはassertを使うと簡単
# assert (条件文) (異なる時に出力するメッセージ)
# 出力はなく、条件を満たせば(=True)そのままプログラムが進行
assert boolChecker("did")
assert not boolChecker("yes")

"""
with open("sentiment.txt") as data:
    lines = data.readlines()
    for line in lines:
        if boolChecker(line):
            print("True")
        else:
            print("False")
        print(line)
"""