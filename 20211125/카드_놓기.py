n = int(input())
k = int(input())

# str로 list에 저장
cards = []
for _ in range(n):
    cards.append(input())

tmp = []    # 임시 저장용
res = set() # 결과 저장용
checkCard = [False] * n


def pick_card(cnt):
    if cnt == k:
        res.add(''.join(map(str, tmp)))
        return
    for i in range(n):
        if not checkCard[i]:
            # card선택 표시
            checkCard[i] = True
            tmp.append(cards[i])
            pick_card(cnt+1)
            tmp.pop()
            # card 선택 초기화
            checkCard[i] = False

pick_card(0)
print(len(res))

'''
from itertools import permutations

n = int(input())
k = int(input())

#str로 list에 저장
cards = []
for _ in range(n):
    cards.append(input())

res = set()
for card in permutations(cards, k):
    res.add(''.join(card))

print(len(res))
'''
