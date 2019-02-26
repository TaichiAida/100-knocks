# coding utf-8
# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．

import plyvel

def searchArea(name):
    db = plyvel.DB("./db_60",create_if_missing=True)
    try:
        area = db.get(name.encode("utf-8")).decode("utf-8")
    except:
        area = "登録なし"
    db.close()
    return area

if __name__ in "__main__":
    while True:
        name = input()
        # 終了条件
        if name == "end":
            break
        else:
            area = searchArea(name)
            print(f"artist:{name}\tarea:{area}")
