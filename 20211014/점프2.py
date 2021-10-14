import sys
input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

temp = [[0] * n for _ in range(n)]
temp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        size = matrix[i][j]
        if i+size < n:
            temp[i+size][j] += temp[i][j]
        if j+size < n:
            temp[i][j+size] += temp[i][j]

print(temp[n-1][n-1])