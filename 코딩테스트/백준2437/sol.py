import sys

input = sys.stdin.readline

n = int(input())

w = list(map(int,input().split()))
w.sort()

answer = 1

for i in range(len(w)):
    if answer >= w[i]:
        answer += w[i] 
    else: 
        break 

print(answer)

