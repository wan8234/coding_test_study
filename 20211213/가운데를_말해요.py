import heapq as hq
import sys
input = sys.stdin.readline

small = []
big = []

n = int(input().strip('\n'))

for i in range(n):
    num = int(input().strip('\n'))
    if len(small) == len(big):
        hq.heappush(small, -num)
    else:
        hq.heappush(big, num)

    if small and big and big[0] < -small[0]:
        bigMin = hq.heappop(big)
        smallMax = -hq.heappop(small)
        hq.heappush(big, smallMax)
        hq.heappush(small, -bigMin)
    print(-small[0])
