import sys

input = sys.stdin.readline

S = input()

answer = 0

def get_pi(P):
    
    m = len(P)
    pi = [0 for i in range(m)]
    idx = 0
    for i in range(1, m):
        while idx > 0 and P[i] != P[idx]: #idx가 0이거나, i와idx의 문자열이 같을때까지 반복
            idx = pi[idx - 1]

        if P[i] == P[idx]: #i와 idx가 같을경우 idx증가
            idx += 1
            pi[i] = idx #i번쨰의 값으로 idx 저장

    return max(pi)


for i in range(len(S)):
    answer = max(answer,get_pi(S[i:]))

print(answer)