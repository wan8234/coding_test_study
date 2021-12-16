import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp_left = [1] * 1000
dp_right = [1] * 1000

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if numbers[i] > numbers[j]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)

maximum = 0
for i in range(N):
    maximum = max(maximum, dp_left[i] + dp_right[i])

print(maximum - 1)