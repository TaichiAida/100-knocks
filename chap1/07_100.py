# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
def response(x,y,z):
    print (x,end = '')
    print ("時の",end = '')
    print (y,end = '')
    print ("は",end = '')
    print (z)

def response2(x,y,z):
    print (str(x) + "時の" + str(y) + "は" + str(z))

x = 12
y = "気温"
z = 22.4
response(x,y,z)
response2(x,y,z)
