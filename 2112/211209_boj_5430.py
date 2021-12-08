from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    oper = list(input().rstrip())
    n = int(input())
    
    nums = list(input().rstrip()[1:-1].split(','))
    queue = deque()
    queue.extend(nums)
    
    idx = 0
    for p in oper:
        if p == 'R':
            if idx == 0:
                idx = -1
            else:
                idx = 0
        else:
            if not queue or n == 0:
                print('error')
                break
            
            if idx == 0:
                queue.popleft()
            else:
                queue.pop()
    else:
        if idx == -1:
            queue.reverse()

        print('[{}]'.format(",".join(queue)))