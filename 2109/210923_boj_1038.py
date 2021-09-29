import sys
input = sys.stdin.readline

n = int(input())
count = -1
answer = -1

def back(position, num):
    global count
    global answer
    if len(num) == position: # digit made
        count += 1
        if count == n:
            answer = int(num)
            print(answer)
            sys.exit()
        return
    else:
        if num == '': # first position of digit
            for i in range(position - 1, 10):
                num += str(i)
                back(position, num)
                num = ''
        else:
            start = position - len(num) - 1 # if position == 4 and len(num) == 2 then next number can be 1 to 7 (32XX ~ 98XX)
            end = int(num[-1])
            for i in range(start, end):
                num += str(i)
                back(position, num)
                num = num[:-1]

for i in range(1, 11): # digit 1st to 11th length
    back(i, '')
print(-1)                


# import sys
# input = sys.stdin.readline

# n = int(input())

# position = 1
# count = 0
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def ltoi(des):
#     strings = [str(i) for i in des]
#     strings = "".join(strings)
#     return int(strings)

# def back(des, position):
#     global count
#     if position == 0:
#         count += 1
#         num.append(ltoi(des))

#         return
        
#     for i in range(des[-1] + 1):
#         if i < des[-1]:
#             des.append(i)
#             back(des, position // 10)
#             des.pop()
        
#         if count >= n:
#             return

# while count < n:
#     for i in range(1, 10):
#         des = [i]
#         back(des, position)

#     position *= 10

# print(num[n - 1])

# 1 2 3 4 5 6 7 8 9 10 20 21 30 31 32 40 41 42