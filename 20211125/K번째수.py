import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

left, right = 1, N*N
answer = N

while left <= right:
    mid = (left+right) // 2
    total = 0
    #mid보다 작은 수 : mid를 행으로 나눴을 때 몫
    for i in range(1, N+1):
        total += min(mid//i, N)
    
    if total >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)