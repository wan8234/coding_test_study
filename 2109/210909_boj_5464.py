from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
place = [0] * n
fee = []
weight = [0]
inout = []

cars = {}
queue = deque()
result = 0

for i in range(n):
    fee.append(int(input()))
for i in range(m):
    weight.append(int(input()))
for i in range(2*m):
    inout.append(int(input()))

for car in inout:
    if car > 0:
        for i in range(n):
            if place[i] == 0:
                place[i] = 1
                cars[car] = i
                result += weight[car] * fee[i]
                break
        else:
            queue.append(car)

    else:
        index = abs(car)        
        place[cars[index]] = 0
        
        if queue:
            wait = queue.popleft()
            place[cars[index]] = 1
            cars[wait] = cars[index]
            result += weight[wait] * fee[cars[index]]
print(result)

#######FAIL0#######
# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# fee = {}
# place = [(i + 1) for i in range(n)]
# use = []
# car = {}
# queue = deque()
# position = {}
# result = 0

# for i in range(n):
#     fee[i + 1] = int(input())
# for i in range(m):
#     car[i + 1] = int(input())
#     position[i + 1] = 0
# for i in range(2*m):
#     index = int(input())
#     if index > 0:        
#         if len(use) != n:
#             use.append(min(place))
#             position[index] = min(place)   
#             result += car[index] * fee[min(place)]         
#             place.remove(min(place))
#         else:
#             queue.append(index)
#     else:
             
#         # result += car[-index] * fee[position[-index]]
#         place.append(position[-index])
#         use.remove(position[-index])
#         position[-index] = 0
#         if queue:
#             i = queue.popleft()
#             use.append(min(place))
#             position[i] = min(place)
#             result += car[index] * fee[min(place)]  
#             place.remove(min(place))

# print(result)

#######FAIL1#######
# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# fee = []
# place = [i for i in range(n)]
# use = []
# car = {}
# queue = deque()
# position = {}
# result = 0

# for i in range(n):
#     fee.append(int(input()))
# for i in range(m):
#     car[i] = int(input())
#     position[i] = 0
# for i in range(2*m):
#     index = int(input())
#     if index > 0:
#         index -= 1
#         if len(use) != n:
#             use.append(min(place))
#             position[index] = min(place)
#             # result += 
#             place.remove(min(place))
#         else:
#             queue.append(index)
#     else:
#         index = -(index)
#         index -= 1
#         result += car[index] * fee[position[index]]
#         place.append(position[index])
#         use.remove(position[index])
#         position[index] = 0
#         if queue:
#             n = queue.popleft()
#             use.append(min(place))
#             position[n] = min(place)
#             place.remove(min(place))

# print(result)

#######FAIL2#######
# # from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# fee = [] # fee per place
# place = [0] * n # parking place flag
# car = [0] # input car
# # queue = deque()
# queue = []
# info = {} # parking data with place index
# result = 0

# for i in range(n):
#     fee.append(int(input()))

# for i in range(m):
#     car.append(int(input()))

# for i in range(2*m):
#     index = int(input())
    
#     if index > 0:
#         queue.append(car[index])
#         if place.count(1) != n:
#             for j in range(n):
#                 if place[j] == 0:
#                     break

#             # cur = queue.popleft()
#             cur = queue.pop(0)
#             info[cur] = j
#             place[j] = 1

#     elif index < 0:
#         index = -index
#         money = info.get(car[index], None)
#         # print(money)
#         if money == None:
#             queue.remove(car[index])
#         else:
#             del info[car[index]]
#             result += fee[money] * car[index]
#             place[money] = 0

#             if queue:  
#                 # cur = queue.popleft()
#                 cur = queue.pop(0)
#                 info[cur] = money
#                 place[money] = 1

# print(result)       



