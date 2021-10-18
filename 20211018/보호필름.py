def check(matrix):
    for i in range(len(matrix[0])):
        temp = 1
        cnt = 0
        for j in range(len(matrix)):
            if cnt >= K:
                break
            if matrix[j][i] == temp:
                cnt += 1
            else:
                temp = matrix[j][i]
                cnt = 1
        else:
            if cnt < K:
                return False
    else:
        return True

def combination(x, change):
    if change.count(-1) == D - k:
        temp = [[x for x in y] for y in matrix]
        for i in range(D):
            if change[i] != -1:
                temp[i] = [change[i]] * W
        if check(temp):
            return True
        else:
            return False
    if x >= D:
        return
    change[x] = 0
    if combination(x+1, change):
        return True
    change[x] = 1
    if combination(x+1, change):
        return True
    change[x] = -1
    if combination(x+1, change):
        return True

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        D, W, K = map(int, input().split())
        matrix = []
        for _ in range(D):
            line = list(map(int, input().split()))
            matrix.append(line)

        change = [-1] * D
        for k in range(0, K+1):
            if combination(0, change) == True:
                print("#", i, " ", k, sep="")
                break