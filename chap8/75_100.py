# coding utf-8

# 73で学習したロジスティック回帰モデルの中で，
# 重みの高い素性トップ10と，
# 重みの低い素性トップ10を確認せよ．

import numpy as np
from stemming.porter2 import stem
import re
import matplotlib as mpl
import matplotlib.pyplot as plt

fname_sentiment = "sentiment.txt"
fname_feature = "feature.txt"

# y:ラベル。+1 = 1, -1 = 0 とする。
# x:データ。素性の数が2979個あるため、2979次元…bowぽくなりそう
# theta:境界線の傾き。素性の数が2979個あるため、2979次元…
# eta:学習率。

# シグモイド関数
def sigmoid(theta,data_x):
    # theta, x is np_array
    # sigmoid is also np_array
    return 1/(1+np.exp(-1*np.dot(data_x,theta)))

# 目的関数logL
def logL(theta,data_x,data_y):
    sigmoid_ = sigmoid(theta,data_x).T
    left = np.dot(data_y,np.log(sigmoid_))
    right = np.dot((1-data_y),np.log(1-sigmoid_))
    #print(f"left:{left}\tright:{right}")
    #print(f"exp_left:{np.exp(left)}\texp_right:{np.exp(right)}")
    #return np.exp(left + right)
    return left + right

# パラメータ更新
def update_theta(theta,data_x,data_y,eta):
    sigmoid_ = sigmoid(theta,data_x)
    slope = sigmoid_ - data_y
    #print(np.dot(data_x.T, slope))
    return theta - eta * np.dot(data_x.T, slope)

# 学習の進捗確認
def learn_progress(progress):
    print(f"{progress}%終了しました。")

# 素性を抽出した時（72本目）と同じように、ストップワード削除＋ステミング
def get_feature(words_splited):
    ans = []
    # Oracle text のストップワード
    stop_words = (
        "a did in only then where "
        "all do into onto there whether "
        "almost does is or therefore which "
        "also either it our these while "
        "although for its ours they who "
        "an from just s this whose "
        "and had ll shall those why "
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
    for word in words_splited:
        if word.lower() not in stop_words and len(word) > 1:
            if "\n" in word:
                word = re.sub(r"\n","",word)
            ans.append(stem(word))
    return ans

# データx,ラベルyの獲得
def get_xy():
    train_y = []
    train_x = []
    #"""
    i = 0
    #"""
    with open(fname_sentiment) as data:
        lines = data.readlines()
        for line in lines:
            words = line.split(" ")

            #"""
            i += 1
            if i > 100:
                break
            #print(words[1:])
            #print(raw_data)
            #print(type(raw_data[0]))
            #"""

            # ラベルyの獲得
            if words[0] == "+1":
                y = 1
            elif words[0] == "-1":
                y = 0
            train_y.append(y)

            raw_data = get_feature(words[1:])
            
            x = []
            with open(fname_feature) as f:
                features = f.readlines()
                # 素性の順番だけは変わらないので、素性の順番でベクトルを作成
                for feature in features:
                    # 素性の前処理
                    if "\n" in feature:
                        feature = re.sub(r"\n","",feature)
                    # 素性があれば1、なければ0
                    if feature in raw_data:
                        x.append(int(1))
                    else:
                        x.append(int(0))
            train_x.append(x)
            #print(f"y:{y}\tx:{x}")

    # 計算を早くするためにnumpyの行列に変換
    train_y = np.array(train_y)
    train_x = np.array(train_x)
    return train_x,train_y


# 学習
def train(eta):

    # シータの初期値設定
    theta = [int(1)]*2979
    theta = np.array(theta)
    data_x,data_y = get_xy()

    for x in range(5000):
        #print(f"loop-{x}-times")
        #print(f"theta:{theta}")
        #print(f"sigmoid:{sigmoid(theta,data_x)}")
        logL_now = logL(theta,data_x,data_y)
        #print(f"logL:{logL(theta,data_x,data_y)}")
        #print(f"L:{np.exp(logL(theta,data_x,data_y))}")
        theta = update_theta(theta,data_x,data_y,eta)
        #print()

        # logLまたはLの最大値を見つけて終了。
        # 1つ前のlogLを取っておき、比較。
        if x != 0 and (logL_now - logL_past) < 0.001:
            print("break")
            break
        # logLの更新
        logL_past = logL_now
    print(f"eta:{eta}\tlogL:{logL_now}\tL:{np.exp(logL_now)}")
    # 学習率etaの最適な値を求めるときだけ以下の返り値
    #return eta, logL_now
    return theta

eta = 1e-1
theta = np.load("theta.npy")
with open(fname_feature) as f:
    features = f.readlines()

# 重みが高い素性top10
# 重みが低い素性top10
# thetaの中で最も大きい/小さい要素のindexを抽出
# 対応するものをfeaturesリストから抽出
print("--max_10_features--")
"""
print(f"max_theta:{theta.max()}")
index_max = theta.argmax()
print(f"max_theta_argmax:{theta[index_max]}")
print(f"max_feature:{features[index_max]}")
"""
list_ = np.argsort(-1*theta)[:10]
for index in list_:
    print(theta[index])
    print(features[index])

print("--min_10_features--")
"""
print(f"min_theta:{theta.min()}")
index_min = theta.argmin()
print(f"min_theta_argmax:{theta[index_min]}")
print(f"min_feature:{features[index_min]}")
"""
list_ = np.argsort(theta)[:10]
for index in list_:
    print(theta[index])
    print(features[index])
