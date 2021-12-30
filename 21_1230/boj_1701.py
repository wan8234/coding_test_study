import sys

input = sys.stdin.readline

S = input()

answer = 0

def get_pi(P):
    
    m = len(P)
    pi = [0 for i in range(m)]
    idx = 0
    
    
    for i in range(1, m):
              
        while idx > 0 and P[i] != P[idx]: 
            idx = pi[idx - 1]

        # i가 가리키는 문자와 idx가 가리키는 문자가 같다면
        # idx를 1증가시키고 pi[i](failure배열)의 값을 1 증가시킨다
        # idx는 가장 길게 매칭된 부분 문자열의 길이
        
        if P[i] == P[idx]: 
            idx += 1
            pi[i] = idx 

    return max(pi)


for i in range(len(S)):
    answer = max(answer,get_pi(S[i:]))

print(answer)
