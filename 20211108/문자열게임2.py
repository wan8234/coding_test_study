import sys
from collections import defaultdict
input = sys.stdin.readline


# 후보가 될 수 있는 알파벳을 구하는 함수
def findCandidate(W, K):
    
    candidate_alphabet = defaultdict(list)  # 후보 알파벳을 저장하는 함수
                                            # {'a': [1,2,3], ~}
    # 어떤 문자를 k개 이상 포함하는 알파벳 추출
    for i in range(len(W)):
        if W.count(W[i]) >= K:
            candidate_alphabet[W[i]].append(i)  # k,v == 알파벳, idx
    if len(candidate_alphabet) == 0:
        return False
    max_length = 1
    min_length = len(W)
    # 문자열을 k개 포함하는 가장 긴 연속 문자열 길이 구하기
    for value in candidate_alphabet.values():   # {'a': [0,2,3,4,6], ~}
        if K != 1:
            for i in range(len(value) - K+1):
                max_length = max(max_length, value[K-1+i] - value[i] + 1 )
                min_length = min(min_length, value[K-1+i] - value[i] + 1 )
        else:
            min_length = 1
            
    return [min_length, max_length]


T = int(input())
arr = []

for i in range(T):
    W = input() # 문자열
    K = int(input()) # 양의 정수 
    arr.append(findCandidate(W, K))

for i in arr:
    if not i:
        print(-1)
    else:
        for j in i:
            print(j, end=' ')
        print()

