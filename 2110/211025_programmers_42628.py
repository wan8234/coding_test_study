import heapq

def solution(operations):
    answer = []
    data = []
    data_max = []
    
    for oper in operations:
        o, num = oper.split()        
        num = int(num)
        
        if o == 'I':
            heapq.heappush(data, num)
            heapq.heappush(data_max, (num * -1, num))
        else:
            if not data:
                continue
            elif num == 1:
                value = heapq.heappop(data_max)[1]
                data.remove(value)
            elif num == -1:
                value = heapq.heappop(data)
                data_max.remove((value * -1, value))
                
    if data:
        answer = [heapq.heappop(data_max)[1], heapq.heappop(data)]
    else:
        answer =[0,0]        
    
    return answer
    
#### FAIL LAST CASE ####
# import heapq

# def solution(operations):
#     answer = []
#     data = []
    
#     for oper in operations:
#         if oper[0] == 'I':
#             o, num = oper.split(' ')
#             data.append(int(num))
#         elif data and oper[0] == 'D':
#             o, num = oper.split(' ')
#             heapq.heapify(data)
            
#             if data and num == '1':
#                 data.pop()
#             elif data and num == '-1':
#                 data.pop(0)
#         print(data)
#     if data:
#         heapq.heapify(data)
#         answer = [data[-1],data[0]]
#     else:
#         answer = [0,0]
#     return answer