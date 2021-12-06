import sys

def calculate(posList):
    global mat

    totVal = 0

    for pos in posList:
        cr = pos // M
        cc = pos % M

        totVal += mat[cr][cc]
    
    return totVal


def search(posList, depth):
    global answer

    if depth == 4:
        totVal = calculate(posList)
        if answer < totVal:
            answer = totVal
        return

    for pos in posList:
        cr = pos // M
        cc = pos % M
        
        for idx in range(3):
            newR = cr+dy[idx]
            newC = cc+dx[idx]

            if 0 <= newR < N and 0 <= newC < M and not newR * M + newC in posList:
                search(posList+[newR * M + newC], depth+1)

                
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().strip().split())

    mat = [ list(map(int, sys.stdin.readline().strip().split())) for _ in range(N) ]
    
    dx = [1, 0, -1]
    dy = [0, 1, 0]
    answer = 0

    for i in range(N):
        for j in range(M):
            search([i*M+j], 1)

    print(answer)