import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

start, end = 1, K
res = 0

while start <= end:
    mid = (start+end) // 2
    tot = 0
    for i in range(1, N+1):
        tot += min(mid//i, N)
    
    if tot < K:
        start = mid + 1
    else:
        res = mid
        end = mid - 1

print(res)
