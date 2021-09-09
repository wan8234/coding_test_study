import sys
from collections import deque


input = sys.stdin.readline

n,m = map(int,input().split())


p_fee = dict()
car_weight = dict()
p_seq = deque()

print(len(p_seq))


for i in range(n):
    p_fee[i+1] = int(input())
    
for j in range(m):
    car_weight[j+1] = int(input())

for k in range(2*m):
    car = int(input())



