from itertools import permutations
import math

def is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 

def solution(numbers):
    answer = 0
    
    p_arr = list()
    ans_arr = list()
    
    for i in range(1,len(numbers)+1):
        for j in list(permutations(numbers,i)):
            p_arr.append(int(''.join(j)))
            
    non_d_arr = list(set(p_arr))
    
    for i in range(len(non_d_arr)):
        if is_prime_num(non_d_arr[i]) :
            if non_d_arr[i] == 1 or non_d_arr[i] == 0:
                pass
            else:
                ans_arr.append(non_d_arr[i])
        else:
            pass
            
    answer = len(ans_arr)
    
    return answer