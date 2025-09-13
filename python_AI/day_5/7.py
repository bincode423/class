import pickle
import numpy as np
from tqdm.auto import tqdm
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from konlpy.tag import Okt

with open("tokenized.pkl", "rb") as f:
    data = pickle.load(f)

tokenized = data["tokenized"]
labels = data["labels"]

print("\n[Word2Vec] 학습 시작")
w2v = Word2Vec(
    sentences=tokenized,
    vector_size=100,
    window=5,
    min_count=5,
    workers=4,
    sg=1,
    negative=5,
    epochs=10,
    seed=42
)
print("[Word2Vec] 어휘 수:", len(w2v.wv))

dim = w2v.vector_size
print("\n[문장 벡터] 평균 임베딩 생성")

X = []
for toks in tqdm(tokenized, total=len(tokenized), desc="Averaging", ncols=80):
    vecs = [w2v.wv[w] for w in toks if w in w2v.wv]
    X.append(np.mean(vecs, axis=0) if vecs else np.zeros(dim))

X = np.array(X)
y = labels


X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
clf = LogisticRegression(max_iter=2000, solver="lbfgs").fit(X_tr, y_tr)

pred = clf.predict(X_te)
print("\nAccuracy:", accuracy_score(y_te, pred))

okt = Okt()
stopwords = {
    "의","가","이","은","들","는","좀","잘","걍","과","도","를","으로","자","에","와","한","하다",
    "에서","에게","께서","보다","부터","까지","처럼","이라","였다","되다","이다"
}
def tokenize(sent: str):
    if not isinstance(sent, str) or not sent:
        return []
    toks = okt.morphs(sent, norm=True, stem=True)
    return [t for t in toks if t not in stopwords and len(t) > 1]

def predict_sentiment(text: str):
    toks = tokenize(text)
    vecs = [w2v.wv[w] for w in toks if w in w2v.wv]
    v = np.mean(vecs, axis=0).reshape(1, -1) if vecs else np.zeros(dim).reshape(1, -1)
    proba = clf.predict_proba(v)[0]
    label = clf.predict(v)[0]
    return {"label": int(label), "proba_neg": float(proba[0]), "proba_pos": float(proba[1]), "tokens": toks}

print(predict_sentiment("ㅋㅋㅋ 노잼"))
print(predict_sentiment("이 영화는 정말 재미없습니다."))