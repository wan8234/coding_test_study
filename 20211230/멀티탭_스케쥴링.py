import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr = deque(arr)

multitap = []
answer = 0
while arr:
    x = arr.popleft()

    #이미 꽂혀있는 경우
    if x in multitap:
        continue

    #멀티 탭에 빈자리가 있는 경우
    elif len(multitap) < N:
        multitap.append(x)

    #하나를 뽑고 꽂아야 하는 경우
    else:
        lastindex = -1
        pickup = -1
        #멀티탭에 꽂혀있는 번호를 검사
        for i in range(len(multitap)):
            #뒤에 쓸 일이 없는 경우, 걔를 바로 뽑아버림
            if multitap[i] not in arr:
                pickup = i
                break
            #다들 뒤에 쓸 일이 있는 경우
            #가장 나중에 쓸 코드를 뽑음
            else:
                index = arr.index(multitap[i])
                if index > lastindex:
                    lastindex = index
                    pickup = i
        
        #뽑고, 새로 꽂기
        multitap.pop(pickup)
        multitap.append(x)
        answer += 1

print(answer)
