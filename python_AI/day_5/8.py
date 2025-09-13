from konlpy.tag import Okt
okt = Okt()
text = "아버지가 방에 들어가신다."
morphs = okt.morphs(text)
print(morphs)

pos = okt.pos(text)
print(pos)