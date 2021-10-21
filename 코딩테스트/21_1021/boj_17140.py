import sys
from collections import Counter

input = sys.stdin.readline

r,c,k = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(3)]

time = 0

def r_operation():

    copy_arr = []
    max_len = 0

    for tmp in arr:

        tmp = Counter(tmp)
        del (tmp[0])

        copy_tmp = sorted(tmp.items(), key=lambda x: (x[1], x[0]))
        tt = []

        for a in copy_tmp:
            tt.extend(a)
            if len(tt) == 100 : break

        max_len = max(max_len,len(tt))
        copy_arr.append(tt)

    for ss in copy_arr:
        ss += [0] * (max_len-len(ss))
    return copy_arr


while True :

    if time > 100 :
        break

    if r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] == k:
        break

    if len(arr)>= len(arr[0]) :

        arr = r_operation()
        
    else :

        arr = list(map(list, zip(*arr)))
        arr = r_operation()
        arr = list(map(list, zip(*arr)))

    time += 1

if time > 100:
    print(-1)

else :
    print(time)