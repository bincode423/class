import random
import gensim.downloader as api

KO2EN = {
    "강아지":"dog","개":"dog","고양이":"cat","곰":"bear","호랑이":"tiger","사자":"lion",
    "코끼리":"elephant","말":"horse","늑대":"wolf","여우":"fox","토끼":"rabbit","사슴":"deer",
    "원숭이":"monkey","침팬지":"chimpanzee","고릴라":"gorilla","판다":"panda","소":"cow",
    "돼지":"pig","양":"sheep","염소":"goat","닭":"chicken","독수리":"eagle","오리":"duck"
}

"""
KO2EN = {
    "사과":"apple","바나나":"banana","포도":"grape","오렌지":"orange","복숭아":"peach",
    "딸기":"strawberry","수박":"watermelon","레몬":"lemon","파인애플":"pineapple","토마토":"tomato",
    "감자":"potato","양파":"onion","당근":"carrot","양배추":"cabbage","상추":"lettuce",
    "오이":"cucumber","쌀":"rice","빵":"bread","치즈":"cheese","버터":"butter",
    "우유":"milk","달걀":"egg","치킨":"chicken","소고기":"beef","돼지고기":"pork",
    "생선":"fish","수프":"soup","샐러드":"salad","피자":"pizza","햄버거":"hamburger"
}
KO2EN = {
    "전화기":"phone","컴퓨터":"computer","노트북":"laptop","책":"book","의자":"chair","테이블":"table","책상":"desk",
    "병":"bottle","컵":"cup","유리컵":"glass","숟가락":"spoon","포크":"fork","칼":"knife","접시":"plate",
    "가방":"bag","배낭":"backpack","지갑":"wallet","시계":"watch","벽시계":"clock","카메라":"camera",
    "텔레비전":"television","라디오":"radio","램프":"lamp","문":"door","창문":"window","열쇠":"key",
    "우산":"umbrella","신발":"shoes","모자":"hat","수건":"towel","비누":"soap","거울":"mirror",
    "침대":"bed","소파":"sofa","베개":"pillow","담요":"blanket","마우스":"mouse","키보드":"keyboard",
    "자전거":"bicycle","손전등":"flashlight","스마트폰":"smartphone","프린터":"printer","리모컨":"remote",
    "선풍기":"fan","에어컨":"air","가위":"scissors","테이프":"tape","지우개":"eraser","연필":"pencil","펜":"pen",
    "종이":"paper","상자":"box","칫솔":"toothbrush","치약":"toothpaste","물병":"water bottle"
}
"""
EN2KO = {v:k for k,v in KO2EN.items()}
print("임베딩 모델 로딩 중... ")
model = api.load("glove-wiki-gigaword-50")
vocab = set(model.key_to_index.keys())

ANIMALS_KO = [ko for ko,en in KO2EN.items() if en in vocab]
MAX_TURNS = 7

def play():
    answer_ko = random.choice(ANIMALS_KO) 
    answer_en = KO2EN[answer_ko]

    print("=== 동물 유사도 퀴즈 ===")
    print("아래 동물들 중 하나가 정답입니다. 맞춰보세요!\n")
    print(", ".join(ANIMALS_KO))
    print(f"\n시도 기회: {MAX_TURNS}번\n")

    for turn in range(1, MAX_TURNS + 1):
        guess_ko = input(f"[{turn}/{MAX_TURNS}] 추측 동물(한글만): ").strip()

        if guess_ko not in ANIMALS_KO:
            print("  - 목록에 없는 동물입니다. 후보 중에서 골라주세요!")
            continue
        if guess_ko == answer_ko:
            print(f"정답! {answer_ko} ({answer_en})")
            return

        guess_en = KO2EN[guess_ko]
        sim = model.similarity(guess_en, answer_en)
        print(f"  - 유사도: {sim:.3f}")
        near = [EN2KO[w] for w,_ in model.most_similar(answer_en, topn=30) 
                if w in EN2KO and EN2KO[w] in ANIMALS_KO and w != answer_en][:3]
        if near:
            print("힌트:", ", ".join(near))
    print(f"\n실패! 정답은 {answer_ko} ({answer_en})")

play()