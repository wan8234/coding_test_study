import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input().rstrip())
delNum = K
answer = []

for i in range(N):
    while delNum > 0 and answer:
        if answer[-1] < num[i]:
            answer.pop()
            delNum -= 1
        else:
            break
    answer.append(num[i])

print(''.join(answer[:N-K]))
