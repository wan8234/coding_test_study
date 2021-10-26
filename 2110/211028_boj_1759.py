# 모음은 최종적으로 확인해야 함. 그렇지 않고 계속 확인할 경우 시간초과.

import sys
input = sys.stdin.readline

L, C = map(int, input().split())
vowels = ['a', 'e', 'i', 'o', 'u']

alpha = list(input().split())
use = [0] * C

answer = []

def dfs(password, idx):
    length = len(password)

    if length == L:
        vow = 0
        for v in range(length):
            if password[v] in vowels:
                vow += 1

        if vow and length - vow >= 2:
            temp = ''.join(password)
            if temp not in answer:
                answer.append(temp)
        return
    if idx == C:
        return

    for i in range(idx, C):
        if use[i] == 0:
            use[i] = 1
            password.append(alpha[i])

            dfs(password, i + 1)

            use[i] = 0
            password.pop()

alpha.sort()
dfs([], 0)

for a in answer:
    print(a)
