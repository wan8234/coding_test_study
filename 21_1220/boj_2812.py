import sys

input =sys.stdin.readline

n,k = map(int,input().split())

num_list = list(input().strip())

stack = list()

for i in range(n):
    while k > 0 and stack:
        if stack[len(stack)-1] < num_list[i]:
            stack.pop()
            k-=1
        else:
            break
    stack.append(num_list[i])
    
print(''.join(stack[:n - k]))