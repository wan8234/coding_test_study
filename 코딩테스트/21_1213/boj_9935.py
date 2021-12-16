import sys


input = sys.stdin.readline

target_string = list(input().rstrip())
bomb_string = list(input().rstrip())

stack =list()

for i in range(len(target_string)):

    stack.append(target_string[i])

    if stack[-1] == bomb_string[-1] and len(stack) >= len(bomb_string):
        if stack[-len(bomb_string):] == bomb_string:
            for i in range(len(bomb_string)):
                stack.pop()

if stack:
    print("".join(stack))
    
else:
    print("FRULA")