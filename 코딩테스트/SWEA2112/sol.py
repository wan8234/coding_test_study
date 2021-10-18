def check(film):
    for j in range(W):
        cnt = 1
        for i in range(1, D):

            if film[i][j] == film[i-1][j]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= K:        
                break

        if cnt < K:             
            return False

    return True                 


def inject_dfs(depth, k, pick):		

    global result

    if result <= depth:           
        return
        
    if depth == pick:       
        if check(film):
            result = min(result, depth)

        return
        
    for i in range(k, D):			
        for d in range(2):			

            select.append(i)
            film[i] = drugs[d]         
            inject_dfs(depth+1, i+1, pick)
            film[i] = raw[i]            
            select.pop()

# D = 두깨 , W = 가로크기 K = 최소 연속 속성수

for tc in range(1,int(input())+1):

    D, W, K = map(int, input().split())

    film = [list(map(int, input().split())) for _ in range(D)]

    raw = [f[:] for f in film]
    drugs = [[0] * W, [1] * W]

    if check(film) == True:   
        result = 0

    else:                       
        result = float('inf')
        select = []

        for pick in range(1, D+1):

            inject_dfs(0, 0, pick)

            if result < float('inf'):   
                break

    print("#{} {}".format(tc, result))