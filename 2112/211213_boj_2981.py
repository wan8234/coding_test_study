import math
import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()
gap = []
result = []

for i in range(1, N):
    gap.append(numbers[i] - numbers[i - 1])

before = gap[0]
for i in range(1, len(gap)):
    before = math.gcd(before, gap[i])

for i in range(2, int(math.sqrt(before)) + 1):
    if before % i == 0:
        result.append(i)
        result.append(before // i)

result.append(before)
result = list(set(result))
result.sort()
print(*result)
