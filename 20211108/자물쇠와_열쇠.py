def solution(key, lock):
    answer = True

    key_up = []
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j] == 1:
                key_up.append((i, j))


    width = (len(key)-1) * 2 + len(lock)
    matrix = [[-1] * width for _ in range(width)]

    lock_down = 0
    
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            matrix[i + len(key) - 1][j + len(key) - 1] = lock[i][j]
            if lock[i][j] == 0:
                lock_down += 1

    def check():
        for i in range(width - len(key) + 1):
            for j in range(width - len(key) + 1):
                cnt = 0
                for x, y in key_up:
                    if matrix[i + x][j + y] == 0:
                        cnt += 1
                    if matrix[i + x][j + y] == 1:
                        break
                if cnt == lock_down:
                    return True
        else:
            return False

    def rotation():
        for i in range(len(key_up)):
            x, y = key_up[i]
            key_up[i] = (y, len(key) - 1 - x)

    if check():
        return True

    for _ in range(3):
        rotation()
        if check():
            return True
    else:
        return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))