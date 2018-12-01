# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ
'''
# 練習
s = "abcdef"
# pythonでcのようにfor(i = 0;i+N <= len(s);i++)は難しい
N = 2   # N-gram
i = 0
while i + N <= len(s):
    print (s[i:i+N])
    i = i + 1
'''

# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成
# 文字グラム
def Ngram_moji(N,s):
    i = 0
    if N > len(s):
        return
    else:
        gram1 = []
        while i + N <= len(s):
            gram1.append(s[i:i+N])
            i = i + 1
        
        # print (gram)
        return gram1

# 単語グラム
def Ngram_tango(N,s):
    t = s.split()
    if N > len(t):
        return
    else:
        j = 0
        gram2 = []
        while j + N <= len(t):
            # 単語をN個足し合わせる
            moji = t[j]
            for x in range(1,N):
                moji = moji + t[j + x]
            '''
            gram2.append(t[j:j+N-1])
            print (t[j:j+N-1])
            '''
            print (moji)
            gram2.append(moji)
            j = j + 1
        return gram2

s = "I am an NLPer"
N = 2

# Ngram(N,s)
result_moji = []
result_moji = Ngram_moji(N,s)
print (result_moji)
result_tango = []
result_tango = Ngram_tango(N,s)
print (result_tango)
