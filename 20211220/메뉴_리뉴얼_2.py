from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        combi = []
        for x in orders:
            temp = list(combinations(sorted(x), c))
            combi += temp
        counter = Counter(combi)
        maxi = 0
        ans = []
        for x in counter:
            if counter[x] > 1:
                if maxi < counter[x]:
                    maxi = counter[x]
                    ans = [''.join(x)]
                elif maxi == counter[x]:
                    ans.append(''.join(x))
        answer += ans
    answer.sort()

    return answer


orders = list(map(str, input().split()))
course = list(map(int, input().split()))
print(solution(orders, course))