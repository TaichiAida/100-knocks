# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

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
def knock36():
    word_List = {}
    neko_txt = knock30()
    for sentence in neko_txt:
        for word in sentence:
            if word["surface"] not in word_List:
                word_List[word["surface"]] = 1
            else:
                word_List[word["surface"]] += 1

    answer = sorted(word_List.items(),key = lambda x:x[1],reverse = True)
    return answer

# 出現頻度の高い順に取得
ans = knock36()

# グラフ化
# zip(*(list)) の * は行と列の変換のようなもの
dic_Zipped = list(zip(*ans))
x_words = dic_Zipped[0]
y_counts = dic_Zipped[1]

# フォントの指定　そのままだと日本語が表示できない為、 AppleGothicを使う
mpl.rcParams["font.family"] = "AppleGothic"

# ヒストグラムの作成
plt.hist(y_counts,range = (1,20))

# タイトル、ラベル編集
plt.title("ヒストグラム")
plt.xlabel("出現頻度")
plt.ylabel("単語の種類")

# 表示
plt.show()
"""
# 読み込めるフォントファイルのリスト
print(matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf'))
# fontの指定できるリスト
print([f.name for f in matplotlib.font_manager.fontManager.ttflist])
"""
