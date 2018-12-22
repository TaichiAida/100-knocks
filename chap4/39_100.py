# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

# グラフを扱うため必要
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

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

# フォントの指定　そのままだと日本語が表示できない為、 AppleGothicを使う
mpl.rcParams["font.family"] = "AppleGothic"

# zip(*(list)) の * は行と列の変換のようなもの
dic_Zipped = list(zip(*ans))
x_words = dic_Zipped[0]
y_counts = dic_Zipped[1]

# 散布図のデータ指定
plt.scatter(
    range(1, len(y_counts) + 1),  # x軸：順位
    y_counts                      # y軸：出現頻度
)

# 対数グラフにする
plt.xscale("log")
plt.yscale("log")

"""
# フォントの指定はこのタイミングで行うと反映されない。ここより前の散布図が関係してる？

# フォントの指定　そのままだと日本語が表示できない為、 AppleGothicを使う
mpl.rcParams["font.family"] = "AppleGothic"
"""

# タイトル、ラベル編集
plt.title("グラフ\n〜Zipfの法則〜")
plt.xlabel("出現度順位")
plt.ylabel("出現頻度")

# 表示
plt.show()
