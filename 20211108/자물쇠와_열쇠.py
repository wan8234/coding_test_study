# 회전 시켰을때 나오는 모양 4가지
    # 상하좌우로 각각 이동
        # 범위 내만 살리고 범위 밖은 버림? 배열을 늘림?
            #Lock과 합쳤을때 모든 요소 값 1


# cos -sin
# sin cos

# 0 -1     -1  0     0 1            
# 1  0      0 -1    -1 0

# -y,x       -x,-y    y, -x
# -------------------------------------------
'''
 (0,0), ... , (0,M-1)                         (0,M-1), (1,M-1), ... , (M-1,M-1)            (M-1,M-1), (M-1,M-2), ... ,(M-1,0)
 (1,0), ... , (1,M-1)                         (0,M-2), (1,M-2), ... , (M-1,M-2)            (M-2, M-1), (, M-2), ... ,(, 0) 
 .                                  =>                                              =>        
 .
 .
 (M-1,0), ... , (M-1,M-1)
 
 ####### (i, j)  -> (j, M-1-i)
 ####### arr[i][j] ->  arr[j, M-1-i]
'''

# 시계방향 90도씩 회전
def turnKey(key):
    M = len(key)
    res = [[0] * M for _ in range(M)]
    
    for i in range(M):
        for j in range(M):
            res[j][M-1-i] = key[i][j]
    return res


#열쇠 맞추기
def trySolve(x, y, key, expand_lock, M):
    for i in range(M):
        for j in range(M):
            expand_lock[x + i][y + j] += key[i][j]

            
#풀렸는지 확인
def check(M, N, expand_lock):
    for i in range(N):
        for j in range(N):
            if expand_lock[M+i][M+j] != 1:
                return False;
    return True
    
            
            
#복구
def recover(x, y, key, expand_lock, M):
    for i in range(M):
        for j in range(M):
            expand_lock[x + i][y + j] -= key[i][j]


def solution(key, lock):
    N = len(lock)
    M = len(key)
    expand_size = N + M *2 # 확장한 Lock 크기
    expand_lock = [[0] * expand_size for _ in range(expand_size)]
    
    # lock 중앙 배치
    for i in range(N):
        for j in range(N):
            expand_lock[M+i][M+j] = lock[i][j]
    
    for turn in range(4):
        #회전
        key = turnKey(key)
        for x in range(M + N):
            for y in range(M + N):
                #맞춰보기
                trySolve(x, y, key, expand_lock, M)
                #확인
                if check(M, N, expand_lock):
                    return True
                else:
                    #복구
                    recover(x, y, key, expand_lock, M)
    return False
