import sys
input = sys.stdin.readline

w, s = map(int, input().split())
token = input().rstrip()
goal = input().rstrip()

w_alpha = [0] * 52
s_alpha = [0] * 52

for i in range(w):
    if 'a' <= token[i] <= 'z':
        w_alpha[ord(token[i]) - ord('a')] += 1
    else:
        w_alpha[ord(token[i]) - ord('A') + 26] += 1

start = 0
length = 0
answer = 0

for i in range(s):
    if 'a' <= goal[i] <= 'z':
        s_alpha[ord(goal[i]) - ord('a')] += 1
    else:
        s_alpha[ord(goal[i]) - ord('A') + 26] += 1
    length += 1
    
    if length == w:
        if w_alpha == s_alpha:
            answer += 1
        if 'a' <= goal[start] <= 'z':
            s_alpha[ord(goal[start]) - ord('a')] -= 1
        else:
            s_alpha[ord(goal[start]) - ord('A') + 26] -= 1
    
        start += 1
        length -= 1

print(answer)
