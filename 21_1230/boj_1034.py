import sys

input = sys.stdin.readline

N,M = map(int,input().split())

lamp = list()

for _ in range(N):
    lamp.append(str(input().rstrip()))

print(lamp)


K = int(input())
max_cnt = 0

for col in range(N):

    zero_count = 0

    for i in lamp[col]:
        
        if i == '0':
            zero_count += 1
        
    light_cnt = 0

    if zero_count <= K and zero_count%2 == K%2:  

        for col2 in range(N):  
            
            if lamp[col] == lamp[col2]:  
                light_cnt += 1  
                
    max_cnt = max(max_cnt, light_cnt)  
    
print(max_cnt)
