import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dic = dict()
    string = input().strip('\n')
    s = list(string)

    K = int(input())

    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]].append(i)
        else:
            dic[s[i]] = [i]


    mini = int(1e9)
    maxi = 0

    no = False
    for x in dic:
        arr = dic[x]
        if len(arr) >= K:
            no = True
            for i in range(len(arr) - K+1):
                temp = arr[i + K -1] - arr[i] + 1
                mini = min(mini, temp)
                maxi = max(maxi, temp)
    
    if not no:
        print(-1)
        continue
    else:
        print(mini, maxi)

