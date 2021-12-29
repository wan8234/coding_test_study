import sys
input = sys.stdin.readline

#KMP 알고리즘
def make_table(pattern):
    length = len(pattern)
    table = [0] * len(pattern)
    j = 0
    for i in range(1, length):
        
        #??
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        #같으면 패턴 + 1 되는 중
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return max(table)

s = input().strip('\n')
result = 0

for idx in range(len(s)):
    sub_str = s[idx:len(s)]
    result = max(result, make_table(sub_str))

print(result)