import sys
from collections import deque


input = sys.stdin.readline

n,m = map(int,input().split())


p_fee = dict() #n
car_weight = dict() #m

p_space = [0 for _ in range(n)]
p_wait = deque(maxlen = 3)

tot_fee = 0

for i in range(n):
    p_fee[i+1] = int(input())
    
for j in range(m):
    car_weight[j+1] = int(input())

for k in range(2*m):
    
    car = int(input())

    if car > 0:
        if len(p_space)
                