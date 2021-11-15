import sys

input = sys.stdin.readline

n = int(input())

n_list = list()

for _ in range(n):
    age,name = map(str,input().split())
    n_list.append((int(age),name))
    
n_list.sort(key = lambda  x:x[0])


for inform in n_list:
    print(inform[0],inform[1])