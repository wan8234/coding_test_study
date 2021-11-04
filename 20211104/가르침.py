import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = []
for _ in range(N):
    word = input().strip('\n')
    words.append(word)


alp = [0] * 26
for x in ['a', 'n', 't', 'i', 'c']:
    alp[25 - (ord('z') - ord(x))] = 1

answer = 0

def dfs(cnt):
    global answer
    if cnt == K - 5:
        can = 0
        for w in words:
            for x in w:
                if alp[25 - (ord('z') - ord(x))] == 0:
                    break
            else:
                can += 1
        answer = max(answer, can)
        return
    
    for i in range(26):
        if alp[i] == 0 and cnt < 26:
            alp[i] = 1
            dfs(cnt + 1)
            alp[i] = 0

if K < 5:
    print(0)    
elif K == 26:
    print(N)
else:        
    dfs(0)
    print(answer)