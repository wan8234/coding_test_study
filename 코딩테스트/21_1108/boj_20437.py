import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    W = input().rstrip()
    K = int(input())

    len_s = len(W)

    a_dict = defaultdict(list)

    for i in range(len_s):

        if W.count(W[i]) >= K:
            a_dict[W[i]].append(i)

    if len(a_dict) == 0:
        print('-1')

    else:
        min_str = 10000
        max_str = 0

        for idx in a_dict.values():
            for j in range(len(idx)-K+1):

                temp = idx[j+K-1] - idx[j] + 1

                if temp < min_str:
                    min_str = temp

                if temp > max_str:
                    max_str  = temp
    
        print(min_str, max_str)