import sys
import collections

input = sys.stdin.readline

n = int(input())

answer = list()

def dfs(n):

    deq = collections.deque()

    for i in range(1,10): #1 ~ 9 까지 값이 들어간 큐 생성
        deq.append((i,str(i)))

    while deq:    

        if len(answer)-1 == n: #
            break

        cur_num,to_num = deq.popleft()

        if cur_num != 0:

            for k in range(cur_num):
                temp = to_num + str(k)
                deq.append((k,temp))
                answer.append((temp))
'''
큐의 맨앞값을 빼서 일의 자리의 수보다 작은 수들을 붙여서 다시 queue에 삽입해준다.
queue = { 2, 3, 4, 5, 6, 7, 8, 9, 10 }
queue = { 3, 4, 5, 6, 7, 8, 9, 10, 20, 21 }
queue = { 4, 5, 6, 7, 8, 9, 10, 20, 21, 30, 31, 32 }'''


for i in range(10): # 입력값이 0~9  dfs 할필요 X 정답 배열에 0~9 넣어줌
    answer.append(i)

if n >=10: # 입력값이 10이상일 때만 dfs
    dfs(n)

if len(answer) > n: #n 이 1023 이하인 경우에만 값 출력 1~9로 만들수있는 감소하는 수의 총 개수가 2^10-1 개 이기 때문
    print(answer[n])
else:
    print(-1)