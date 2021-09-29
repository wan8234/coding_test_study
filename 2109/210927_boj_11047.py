import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
count = 0

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse = True)

for c in coin:
    temp = k // c
    count += temp
    k -= temp * c
    if k == 0:
        break
print(count)