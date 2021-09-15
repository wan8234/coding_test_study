import heapq,sys
from collections import defaultdict


input = sys.stdin.readline

t = int(input())

for _ in range(t):

    max_heap = list()
    min_heap = list()

    input_dic = defaultdict(int)

    k = int(input())

    for _ in range(k):

        oper,num = input().split()
        answer = list()

        if oper == 'I':

            heapq.heappush(max_heap,-int(num))
            heapq.heappush(min_heap,int(num))
            
            input_dic[int(num)] += 1

        elif oper == 'D':

            if num == '1': # delete max num
                while max_heap:
                    key = -heapq.heappop(max_heap) # pop max num
                    if input_dic.get(key):
                        input_dic[key] -= 1 #if dic has key, delete key from dic
                        break

            else: # delete min num
                while min_heap:
                    key = heapq.heappop(min_heap) # pop min num
                    if input_dic.get(key):
                        input_dic[key] -=1
                        break

    for k,v in input_dic.items(): 
        if input_dic[k] != 0: 
            answer.append(k)

    if answer:
        answer.sort()
        print(answer[-1],answer[0])
    else:
        print('EMPTY')