# 単語に分解
# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字
# それ以外の単語は先頭に2文字を取り出す
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
moji = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# 単語に分解
words = moji.split()
# print (words[2][:1])

# 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字
# それ以外の単語は先頭の2文字を取り出す
dictionary = [] # リストの初期化
count = 1   # 先頭から何番目
for word in words:
    if count == 1 or count == 5 or count == 6 or count == 7 or count == 8 or count == 9 or count == 15 or count == 16 or count == 19:
        dictionary.append(word[:1])
        #count = count + 1
    else:
        dictionary.append(word[:2])
        #count = count + 1
    count = count + 1
# print (dictionary)

# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成
result = {} # 辞書型の定義
# result['1'] = dictionary[0] # 追加
for x in range(20):
    result[x+1] = dictionary[x]

print (result) 
