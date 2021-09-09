from collections import deque

n,k = map(int,input().split())

j = deque([i for i in range(1, n + 1)])

result = list()

while len(j) > 0 :
    
    for _ in range(k-1):
        j.append(j.popleft())

    result.append(j.popleft())


res_str = str(result)[1:-1]
print('<',end="")
print(res_str,end="")
print('>')

