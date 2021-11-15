import sys


input = sys.stdin.readline

len_w, len_s = map(int,input().split())

w = input().rstrip()
s = input().rstrip()

start,length,answer = 0,0,0

w_a = [0] * 58 #65 - 90 소문자, 97 - 122 대문자
s_a = [0] * 58

for i in w:
    w_a[ord(i) - ord('A')] += 1

for i in range(len_s):

    s_a[ord(s[i]) - ord('A')] += 1

    length += 1
    
    if length == len_w:

        if w_a == s_a:
            answer += 1

        length -= 1

        s_a[ord(s[start]) - ord('A')] -= 1 
        
        start += 1
        
    
print(answer)