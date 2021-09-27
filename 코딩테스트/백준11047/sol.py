import sys

input = sys.stdin.readline


n,k = map(int,input().split())

coin_lst = list()
cnt = 0


for _ in range(n):
    coin_lst.append(int(input()))


coin_lst.sort(reverse = True)


'''
for i in range(len(coin_lst)):
    cnt += k//coin_lst[i]
    k %= coin_lst[i]
'''

for i in coin_lst:
    cnt += k//i
    print(cnt)
    k %= i

print(cnt)
