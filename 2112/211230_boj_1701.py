import sys
input = sys.stdin.readline

string = input().rstrip()
result = 0

def check(tok):
    table = [0] * len(tok)
    j = 0
    for i in range(1, len(tok)):
        while j > 0 and tok[i] != tok[j]:
            j = table[j - 1]
    
        if tok[i] == tok[j]:
            j += 1
            table[i] = j
    return table

for idx in range(len(string)):
    token = string[idx:len(string)]
    result = max(result, max(check(token)))

print(result)