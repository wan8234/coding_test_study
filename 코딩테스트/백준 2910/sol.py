import sys
from collections import defaultdict

input = sys.stdin.readline

n,c = map(int,input().split())
msg = list(map(int,input().split()))

freqdic = defaultdict(int)

for i in range(len(msg)):
    freqdic[msg[i]] += 1

freqlist = list(freqdic.items())

freqlist.sort(key = lambda x: (-x[1]))

sortedlist = list()

for i in range(len(freqlist)):
    for j in range(freqlist[i][1]):
        sortedlist.append(freqlist[i][0])

print(*sortedlist)