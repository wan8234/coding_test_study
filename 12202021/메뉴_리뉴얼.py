from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        pre_course_list = []
        for menu_list in orders:
            # 가능한 조합 모두 저장
            test_course = combinations(menu_list, i)
            for combi in test_course:
                # pre_course_list : 가능한 조합들 모음 list
                pre_course_list.append(''.join(sorted(combi)))
        #print(pre_course_list)
        # 빈도 저장
        pre_course_list_dict = Counter(pre_course_list).most_common()
        print(pre_course_list_dict)
        for pre_course, cnt in pre_course_list_dict:
            # 가장 많이 주문된 후보를 선정
            if cnt > 1 and cnt == pre_course_list_dict[0][1]:
                answer.append(pre_course)
    answer.sort()
    return answer
            
