import sys
input = sys.stdin.readline

N,K = map(int,input().split())
M = len(str(N))
res = -1

q = set()
q.add((str(N), K))

while q:
    a, k = q.pop()
    if k == 0:
        res = max(res,int(a))
        continue
    k -= 1

    for i in range(M):
        for j in range(i+1, M):
            arr = list(a)
            arr[i], arr[j] = arr[j], arr[i]
            s = ''.join(arr)

            if s[0] == '0': 
                continue
            q.add((s, k))

print(res)
