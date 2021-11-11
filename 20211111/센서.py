import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

s = list(map(int, input().split()))
s.sort()

#센서 간 거리
d = []
for i in range(N - 1):
    d.append(s[i+1] - s[i])

d.sort(reverse=True)

#거리가 먼 경우를 K-1개 삭제해서 K개의 묶음을 만들기
print(sum(d[K-1:]))