import sys
input = sys.stdin.readline

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        break
    line = list(map(int, input().split()))
    
    for i in range(1, n):
        new = list(map(int, input().split()))
        if i == 1:
            new[0] = new[0] + line[1]
            new[1] = min(new[1] + line[1], new[1] + line[1] + line[2], new[1] + new[0])
            new[2] = min(new[2] + line[1], new[2] + line[1] + line[2], new[2] + new[1])

        else:
            new[0] = min(new[0] + line[0], new[0] + line[1])
            new[1] = min(new[1] + min(line), new[1] + new[0])
            new[2] = min(new[2] + min(line[1:3]), new[2] + new[1])

        
        line = new[:] 
    
    print(cnt, ". ", line[1], sep="")
