import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dic = dict()
    string = input().strip('\n')
    s = list(string)

    K = int(input())

    #딕셔너리 
    #키: 알파벳 / 값: 인덱스 배열
    #알파벳이 인덱스 몇번에 있는지 저장
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
        #인덱스 개수가 K개 이상이면
        if len(arr) >= K:
            no = True
            #구해야할 것 1. K개를 포함하는 가장 짧은 / 2. K개를 포함하고 앞 뒤가 해당 문자로 같은 가장 긴
            #둘 다 K개를 포함하면서 앞뒤에 위치해야함
            for i in range(len(arr) - K+1):
                #K개를 포함하도록 하면서 길이 구하기
                temp = arr[i + K -1] - arr[i] + 1
                mini = min(mini, temp)
                maxi = max(maxi, temp)
    
    #K개 이상인게 하나도 없으면
    if not no:
        print(-1)
        continue
    else:
        print(mini, maxi)

