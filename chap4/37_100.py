# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

# グラフを扱うため必要
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager

# 30のプログラム
def knock30():
    text = []
    interim = []
    with open("neko.txt.mecab") as data:
        lines = data.readlines()
        for line in lines:
            if line[0:3] == "EOS":
                if len(interim) > 0:
                    text.append(interim)
                    interim = []
            else:
                contents = line.split("\t")
                words = contents[1].split(",")
                dic = {}
                dic["surface"] = contents[0]
                dic["bace"] = words[6]
                dic["pos"] = words[0]
                dic["pos1"] = words[1]
                interim.append(dic)
    return text

# 36のプログラム
# 出現頻度の高い上位 num 個を返す関数
def knock36(num):
    word_List = {}
    neko_txt = knock30()
    for sentence in neko_txt:
        for word in sentence:
            if word["surface"] not in word_List:
                word_List[word["surface"]] = 1
            else:
                word_List[word["surface"]] += 1

    answer = sorted(word_List.items(),key = lambda x:x[1],reverse = True)
    return answer[0:num]

# 出現頻度の高い上位10個を取得
ans = knock36(10)
print(ans)

# グラフ化
# zip(*(list)) の * は行と列の変換のようなもの
dic_Zipped = list(zip(*ans))
x_words = dic_Zipped[0]
y_counts = dic_Zipped[1]

# フォントの指定　そのままだと日本語が表示できない為、 AppleGothicを使う
mpl.rcParams["font.family"] = "AppleGothic"

# 棒グラフの作成
plt.bar(x_words,y_counts)
plt.show()
"""
# 読み込めるフォントファイルのリスト
print(matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf'))
# fontの指定できるリスト
print([f.name for f in matplotlib.font_manager.fontManager.ttflist])
"""
