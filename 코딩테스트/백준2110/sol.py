import sys

input = sys.stdin.readline


n,c = map(int,input().split())

homelist = list()

for _ in range(n):
    homelist.append(int(input()))

homelist.sort()

start, end = 1, homelist[-1] - homelist[0]
answer = 0

while start <= end:

    mid = (start+end)//2
    idx,count = 0,1

    for i in range(1,len(homelist)):

        if homelist[idx] + mid <= homelist[i]:
            count += 1
            idx = i

    if count < c:
        end = mid - 1
    elif count >= c:
        answer = mid
        start = mid +1

print(answer)
