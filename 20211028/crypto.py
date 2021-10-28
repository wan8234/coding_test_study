import itertools

L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()
moem = ['a', 'e', 'i', 'o', 'u']

comb = list(itertools.combinations(alphabet, L))

for string in comb:
    cnt = 0 
    # 모음 갯수 세기
    for word in string:
        if word in moem:
            cnt += 1
    
    if cnt >= 1 and (L - cnt) >= 2:
        print(''.join(string))

