import heapq
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    oper = []
    data_min = []
    data_max = []
    count = {} # for check whether it was popped or not

    for j in range(k):
        oper.append(input())
    
    for o in oper:
        todo, num = o.split()
        num = int(num)
        
        if todo == 'I':
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            heapq.heappush(data_min, num)
            heapq.heappush(data_max, -num)
            
        elif todo == 'D':
            if num == -1: 
                while data_min:
                    n = heapq.heappop(data_min)
                    if n in count and count[n] > 0:
                        count[n] -= 1
                        if not count[n]:
                            del count[n]
                        break

            elif num == 1:
                while data_max:
                    n = -heapq.heappop(data_max)
                    if n in count and count[n] > 0:
                        count[n] -= 1
                        if not count[n]:
                            del count[n]
                        break    

    if count == {}:
        print("EMPTY")
    else:
        result = sorted(count.items())
        print(result[-1][0], result[0][0])


####FAIL(time over)####
# import heapq
# import sys

# input = sys.stdin.readline

# t = int(input())

# for i in range(t):
#     k = int(input())
#     oper = []
#     data = []

#     for j in range(k):
#         oper.append(input())
    
#     for o in oper:
#         todo, num = o.split()
#         num = int(num)

#         if todo == 'I':
#             data.append(num)
#             heapq.heapify(data)
#         elif todo == 'D' and data != []:
#             if num == -1:                
#                 heapq.heappop(data)
#             elif num == 1:
#                 data = heapq.nlargest(len(data), data)[1:]
#                 heapq.heapify(data)               
    
#     if data == []:
#         print("EMPTY")
#     else:
#         mi = heapq.heappop(data)
#         ma = heapq.nlargest(len(data), data)[0]
#         print(mi, ma)

