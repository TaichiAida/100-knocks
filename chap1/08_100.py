# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''
s = "a"
t = ord(s)
print (int(t)+1)
'''

def cipher():
    # inputには文字列として定義される
    s = input()
    i = 0 
    while i < len(s):
        code = ord(s[i])
        if code > 96 and code < 123:
            print (chr(219 - code),end = "")

        else:
            print (chr(code),end = "")

        i = i + 1
    print()

cipher()
