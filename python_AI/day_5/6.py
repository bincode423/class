import pandas as pd
import urllib.request
from konlpy.tag import Okt
from tqdm import tqdm
import re, os, pickle, urllib.request
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt", filename="ratings.txt")
train_data = pd.read_table('ratings.txt')
TOKEN_FILE = "tokenized.pkl"

print('리뷰 개수 :',len(train_data))
print(train_data.head())

train_data = train_data.dropna(how="any").reset_index(drop=True)
print(len(train_data))
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","", regex=True)
train_data["document"] = train_data["document"].str.replace(r"\s+", " ", regex=True).str.strip()

okt = Okt()
stopwords = {
    "의","가","이","은","들","는","좀","잘","걍","과","도","를","으로","자","에","와","한","하다",
    "에서","에게","께서","보다","부터","까지","처럼","이라","였다","되다","이다"
}
tokenized_data = []

def tokenize(sent: str):
    if not isinstance(sent, str) or not sent:
        return []
    toks = okt.morphs(sent, norm=True, stem=True)
    return [t for t in toks if t not in stopwords and len(t) > 1]

print("[토큰화] 진행 중...")
tokenized = [tokenize(s) for s in tqdm(train_data["document"], total=len(train_data), desc="Tokenizing", ncols=80)]
labels = train_data["label"].astype(int).to_numpy()

# 4) 저장
with open(TOKEN_FILE, "wb") as f:
    pickle.dump({"tokenized": tokenized, "labels": labels}, f)

print(f"[저장 완료] {TOKEN_FILE}")

for i in range(3):
    print(f"\n원문: {train_data['document'][i]}")
    print(f"토큰화: {tokenized[i]}")
    print(f"레이블: {labels[i]}")