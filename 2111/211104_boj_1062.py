# a c i n t
# a b c d e f g h i j k l m n o p q r s t u v w x y z

from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = [input().rstrip() for _ in range(N)]
base = {'a', 'c', 'i', 'n', 't'}
words = []

for d in data:
    words.append(set(d[4:-4]).difference(base)) # set(d[4:-4]) - base 로 해도 같은 결과 (차집합)

alpha = {key: value for value, key in enumerate(set(map(chr, range(ord('a'), ord('z') + 1))).difference(base))}

def change_to_bin(word):
    binary = 0b0
    for w in word:
        binary = binary | (1 << alpha[w])
    return binary

answer = 0
if K < 5:
    print(answer)
else:
    bin = [change_to_bin(word) for word in words]
    pow_two = [2 ** i for i in range(21)]

    for comb in combinations(pow_two, K - 5):
        total = sum(comb)
        count = 0
        for num in bin:
            if num & total == num:
                count += 1

        answer = max(answer, count)
    
    print(answer)
    

#### USING DFS ####
# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())

# if k < 5:
#     print(0)
#     exit()

# elif k == 26:
#     print(n)
#     exit()

# answer = 0
# words = [set(input().rstrip()) for _ in range(n)]
# learn = [0] * 26

# for c in ('a', 'c', 'i', 'n', 't'):
#     learn[ord(c) - ord('a')] = 1

# def dfs(idx, cnt):
#     global answer

#     if cnt == k - 5:
#         read_cnt = 0
#         for word in words:
#             check = True
#             for w in word:
#                 if not learn[ord(w) - ord('a')]:
#                     check = False
#                     break
#             if check:
#                 read_cnt += 1
#         answer = max(answer, read_cnt)
#         return

#     for i in range(idx, 26):
#         if not learn[i]:
#             learn[i] = True
#             dfs(i, cnt + 1)
#             learn[i] = False

# dfs(0, 0)
# print(answer)


#### CANNOT SOLVE ####
# answer = 0
# alpha = [0] * 26
# a_value = ord('a')

# alpha[ord('a') - a_value] = 1
# alpha[ord('c') - a_value] = 1
# alpha[ord('i') - a_value] = 1
# alpha[ord('n') - a_value] = 1
# alpha[ord('t') - a_value] = 1

# if K < 5:
#     print(0)
#     exit()

# K -= 5

# def check():
#     result = 0
#     for word in words:
#         w = word[4:-4]

#         for a in w:
#             if not alpha[ord(a) - a_value]:
#                 break
#         else:
#             result += 1
    
#     return result

# for i in range(N):
#     visit = [0] * N
#     visit[i] = 1
    
#     w = words[i][4:-4]
#     temp = set(w)

#     if len(temp) <= K:
#         for t in temp:
#             if alpha[ord(t) - a_value] == 0:
#                 alpha[ord(t) - a_value] = 1
#                 K -= 1

#     if K == 0:
#         for j in range(N):
#             check(i)

