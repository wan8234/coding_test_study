import sys,bisect


input = sys.stdin.readline

n = int(input()) #size of seq

seq = list(map(int, input().split()))

answer = list([0])


for i in seq:
    if answer[-1] < i:
        answer.append(i)
    else:
        answer[bisect.bisect_left(answer,i)] = i

print(len(answer)-1)

