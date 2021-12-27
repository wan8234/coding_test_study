import sys

input = sys.stdin.readline


N,K = map(int,input().split())

M = len(str(N))

answer = -1

q = set()
q.add((str(N), K))

while q:
    
    a, k = q.pop()

    # 교환 횟수가 남지 않았다면 answer과 비교해서 더 큰 수를 answer에 넣는다.
    if k == 0:
        answer = max(answer,int(a))
        continue

    k -= 1

    for i in range(M):
        for j in range(i+1, M):

            arr = list(a)

            # i번째와 j번째 자릿수를 변경
            arr[i], arr[j] = arr[j], arr[i]
            s = ''.join(arr)

            # 첫 번째 자리가 0이 아닐시
            if s[0] == '0': 
                continue

            q.add((s, k))

print(answer)