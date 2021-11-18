import sys
input = sys.stdin.readline
from collections import deque

#이분 그래프: 인접한 노드가 같은 그룹에 속하지 않게 두 그룹으로 나눌 수 있는 그래프
#이분 그래프 검사: 기준 노드에게 그룹 1을 부여하고, 기준 노드와 인접한 노드는 그룹 -1을 부여
#               진행하면서 인접한 노드와 기준 노드가 같은 그룹에 속하게 되는 경우는 이분 그래프가 아님

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    check = [0] * (V+1)
    line = [[] for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        line[x].append(y)
        line[y].append(x)

    dq = deque()
    
    answer = True
    for i in range(1, V+1):
        if len(line[i]) != 0:
            #방문하지 않은 곳
            if check[i] == 0:
                dq.append(i)
                check[i] = 1

            while dq:
                #기준 노드 pop
                nod = dq.popleft()
                #인접한 노드 모두 검사
                for x in line[nod]:
                    #방문하지 않은 경우 
                    if check[x] == 0:
                        dq.append(x)
                        #기준 노드와 다른 값 부여
                        check[x] = -check[nod]
                    #방문했던 노드가 기준 노드와 값이 같은 경우 : 이분 노드가 아님
                    elif check[x] == check[nod]:
                        answer = False

            if answer == False:
                break
            
    if answer: print("YES")
    else: print("NO")