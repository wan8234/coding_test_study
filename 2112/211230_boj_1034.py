import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lamp = [list(input().rstrip()) for _ in range(N)]

K = int(input())
maximum = 0

for x in range(N):
    zero_cnt = 0

    for num in lamp[x]:
        if num == '0':
            zero_cnt += 1

    same_cnt = 0

    if zero_cnt <= K and zero_cnt % 2 == K % 2:
        for y in range(N):
            if lamp[x] == lamp[y]:
                same_cnt += 1

    maximum = max(maximum, same_cnt)

print(maximum)