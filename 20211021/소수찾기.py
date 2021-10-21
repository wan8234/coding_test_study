from itertools import permutations

def sosu(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        last = round(num ** 0.5) + 1
        for i in range(3, last, 2):
            if num % i == 0:
                return False
    return True

def solution(numbers):
    answer = 0
    ans_list = []
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        nums = list(permutations(numbers, i+1))
        for x in nums:
            
            x = int(''.join(x))
            if x not in ans_list and sosu(x):
                ans_list.append(x)
    return len(ans_list)

print(solution("17"))