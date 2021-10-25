import sys

input = sys.stdin.readline

n = int(input())

top = list(map(int,input().split()))
ts= list()
answer = [0 for _ in range(n)]


for i in range(len(top)):
    
    while ts:
        
        if ts[-1][1] > top[i]:
            answer[i] = ts[-1][0]
            break

        else:
            ts.pop()

    ts.append([i+1,top[i]])

print(*answer)


#time out

'''
input = sys.stdin.readline

n = int(input())

top = list(map(int,input().split()))
top_stack = list(reversed(top))
answer = [0 for _ in range(n)]


for i in range(len(top)):
    for j in range(i,len(top)):
        if top_stack[j] > top_stack[i]:
            answer[i] = top.index(top_stack[j]) + 1
            break

print(*list(reversed(answer)))'''
    