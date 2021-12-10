import sys
input = sys.stdin.readline

S = list(input().rstrip())
token = list(input().rstrip())

s_length = len(S)
t_length = len(token)

stack = []

for i in range(s_length):
    stack.append(S[i])

    if stack[-1] == token[-1] and s_length >= t_length:
        if stack[-t_length:] == token:
            for j in range(t_length):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
