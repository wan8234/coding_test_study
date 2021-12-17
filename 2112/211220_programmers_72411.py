from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        comb = []
        for order in orders:
            for co in combinations(order, c):
                co = list(co)
                co.sort()
                comb.append(''.join(co))
        count = Counter(comb)
            
        if count and max(count.values()) != 1:
            for key in count.keys():
                if max(count.values()) == count[key]:
                    answer.append(key)
        
    answer.sort()
    
    return answer