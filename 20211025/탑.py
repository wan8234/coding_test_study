import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
stack = []
result = []
for i in range(n):
    while stack:
        if stack[-1][1] > line[i]:
            result.append(stack[-1][0] + 1)
            stack.append([i, line[i]])
            break
        else:
            stack.pop()
    else:
        result.append(0)
        stack.append([i, line[i]])
        
#스택 이용
#스택 맨 뒤 보다 작으면 result에 값, 스택에 값
#크면 스택 pop 반복
#스택 비면 result에 0, 스택에 값

for x in result:
    print(x, end=" ")
