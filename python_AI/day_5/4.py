from gensim.models import Word2Vec

corpus = [
    ["고양이", "는", "동물", "이다"],
    ["고양이", "는", "생선", "을", "좋아한다"],
    ["강아지", "는", "동물", "이다"],
    ["강아지", "는", "뼈", "를", "좋아한다"],
    ["고양이", "와", "강아지", "는", "귀엽다"],
    ["사과", "는", "과일", "이다"],
    ["바나나", "는", "과일", "이다"],
    ["포도", "는", "과일", "이다"],
    ["사과", "와", "바나나", "는", "맛있다"],
]

w2v = Word2Vec(
    sentences=corpus,
    vector_size=50,
    window=2,
    min_count=1,
    sg=1,
    negative=5,
    epochs=200,
    seed=42
)

print("유사도(고양이, 강아지):", w2v.wv.similarity("고양이", "강아지"))
print("유사도(사과, 바나나):", w2v.wv.similarity("사과", "바나나"))

print("\n'고양이'와 비슷한 단어 top-5:")
for w, s in w2v.wv.most_similar("고양이", topn=5):
    print(f"{w}: {s:.3f}")