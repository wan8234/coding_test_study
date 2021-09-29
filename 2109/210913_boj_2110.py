import sys
input = sys.stdin.readline

n, c = map(int, input().split())
home = []
for i in range(n):
    home.append(int(input()))

home.sort()
result = 0

def count_home(distance):
    count = 1
    current = home[0]
    for i in range(1, n):
        if home[i] >= current + distance:
            count += 1
            current = home[i]
    return count

start = 1
end = home[-1] - home[0]

while start <= end:
    mid = (start + end) // 2
    count = count_home(mid)
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

