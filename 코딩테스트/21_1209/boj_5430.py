import sys
from collections import deque

input = sys.stdin.readline

t = int(input())


for i in range(t):

    operation = str(input())

    n = int(input())

    flag = 1

    rev_count = 0

    if n == 0:
        temp = input()
        arr = deque()

    else:
        arr = deque(input().rstrip()[1:-1].split(','))

    
    for i in range(len(operation)):

        if operation[i] == 'R':
            rev_count += 1

        elif operation[i] == 'D':
            if len(arr) > 0:
                if rev_count % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                flag = 0
                break

    if flag:
        if rev_count % 2 == 0:
            print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("["+",".join(arr)+"]")

