####use sum function > success // use for loop > fail(only pypy3 can solve)####
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

left = 0
right = max(tree)
result = max(tree)

while left <= right:
    mid = (left + right) // 2

    temp = 0
    # for t in tree:
    #     if t > mid:
    #         temp += (t - mid)
        
    temp = sum([(t - mid) for t in tree if t >= mid])

    if temp >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)