import sys
input = sys.stdin.readline

n = int(input())
result = 0

col = [0] * n
row = [0] * n
ltor = [0] * (n * 2 - 1) # col - row + n - 1
rtol = [0] * (n * 2 - 1) # col + row

def back(x):
    global result
    for y in range(n):
        if row[y] == 0 and ltor[x - y + n - 1] == 0 and rtol[x + y] == 0:
            col[x] = 1
            if x == n - 1:
                result += 1
            else:
                row[y] = ltor[x - y + n - 1] = rtol[x + y] = 1
                back(x + 1)
                row[y] = ltor[x - y + n - 1] = rtol[x + y] = 0

back(0)
print(result)
