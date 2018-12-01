# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求める
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

N = 2
s1 = "paraparaparadise"
s2 = "paragraph"

X = []
Y = []

X = Ngram_moji(N,s1)
Y = Ngram_moji(N,s2)

# 確認 ok
print (X)
print (Y)

# XとYの和集合，積集合，差集合を求める
XorY = []
XandY = []
XdifY = []
YdifX = []

# 積集合
i = 0
while i < len(X):
    # XとYの共通要素
    if X[i] in Y:
        if X[i] in XandY:
            i = i + 1
            continue

        else:           
            XandY.append(X[i])

    i = i + 1
    
print (XandY)

# 和集合
i = 0
while i < len(X):
    if X[i] in XorY:
        i = i + 1
        continue
    else:
        XorY.append(X[i])
    i = i + 1

j = 0
while j < len(Y):
    if Y[j] in XorY:
        j = j + 1
        continue
    else:
        XorY.append(Y[j])
    
    j = j + 1

print (XorY)

# 差集合
i = 0
j = 0
while i < len(X):
    if X[i] in XandY:
        i = i + 1
        continue
    else:
        XdifY.append(X[i])
    i = i + 1

while j < len(Y):
    if Y[j] in XandY:
        j = j + 1
        continue
    else:
        YdifX.append(Y[j])
    j = j + 1

print (XdifY)
print (YdifX)

# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
if "se" in X:
    print ("X is true")
else:
    print ("X is false")

if "se" in Y:
    print ("Y is true")
else:
    print ("Y is false")

# 解答
# setを用いて集合を作成
X = set(X)
Y = set(Y)
print ('XandY: ' + str(X & Y))
print ('XorY: ' + str(X | Y))
print ('X-Y' + str(X - Y))
