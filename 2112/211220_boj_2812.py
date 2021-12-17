import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = list(input().rstrip())
stack = []
count = K

for num in number:
    num = int(num)
    while stack and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

print(''.join(map(str, stack[:N - count])))