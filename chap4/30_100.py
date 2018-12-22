# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．

# 形態素解析し、結果をneko.txt.mecabとして保存
# 結果は「表層形 \t 品詞, 品詞細分類1, 品詞細分類2, 品詞細分類3, 活用型, 活用形, 原形, 読み, 発音」の順
'''
$ mecab
$ mecab neko.txt > neko.txt.mecab
'''

# 形態素解析結果を読み込む
answer = []
interim = []

with open("neko.txt.mecab") as data:
    lines = data.readlines()
    for line in lines:
        if line[0:3] == "EOS":
            # EOS ~ EOSまでが1文
            # interim に何か入っていれば answer に格納、 interim 初期化
            if len(interim) > 0:
                answer.append(interim)
                interim = []
        else:
            contents = line.split("\t")
            words = contents[1].split(",")
            # 辞書に格納していく
            # 辞書型はここで宣言しないと、interimの中も一緒に更新される
            dic = {}
            dic["surface"] = contents[0]
            dic["bace"] = words[6]
            dic["pos"] = words[0]
            dic["pos1"] = words[1]
            # 1文になるまで（EOSまで）interimに保存
            interim.append(dic)
    print(answer)
