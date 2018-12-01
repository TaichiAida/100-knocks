s = "stressed"
"""
# スライスを使ってみる
print (s) 
print (s[0:8])
print (s[-4:-1])
print (s[-8:])
print  (s[:-1])
print (s[8:0])
print (s[-1:8])
print (s[7:8]+s[6:7])
print (s[0:7:1])
print (s[7:0:-1])
print (s[7::-1])

# replace()を使ってみる
print (s.replace("st","dd"))
print (s)   #置き換えても元の文字列は変わらない
s = s.replace(s[0],s[7])    #s=にすると元の文字列を変換可能
print (s)

s = "stressed"
for x in range(0,3):    # 0 <= x < 3
    t = s[x]
    s = s.replace(s[x],s[7-x])
    s = s.replace(s[7-x],t)
    # 1回目 dtredded stresses
    # 2回目 seresses strtssts
    # 3回目 ststssts rtrtrrtr

print (s)
"""
print (s[::-1])
