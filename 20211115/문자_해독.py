import sys
input = sys.stdin.readline

g, s = map(int, input().split())
W = input().strip('\n')
S = input().strip('\n')

answer = 0

word = [0] * 58
part = [0] * 58


for i in range(g):
    w_index = ord('z') - ord(W[i])
    word[w_index] += 1
    s_index = ord('z') - ord(S[i])
    part[s_index] += 1

print(word, part)

for i in range(g, s):
    index = ord('z') - ord(S[i])
    last = ord('z') - ord(S[i-g])
    part[last] -= 1
    part[index] += 1
    if word == part:
        answer += 1

print(word, part)
print(answer)


