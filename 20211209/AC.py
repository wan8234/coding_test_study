import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    p = input().strip('\n')
    n = int(input())
    x = input().strip('\n')
    if n == 0:
        arr = []
    else:
        arr = list(map(int, list(x[1:-1].split(','))))
    arr = deque(arr)

    R = 0
    for x in p:
        if x == 'R':
            if R == 0:
                R = 1
            else:
                R = 0
        else:
            if arr:
                if R == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                break
    else:
        if R == 1:
            arr.reverse()
        print(list(arr))
