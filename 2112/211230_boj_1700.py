import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = list(map(int, input().split()))

plugs = []
cnt = 0

for i in range(K):
    if things[i] in plugs:
        continue

    if len(plugs) < N:
        plugs.append(things[i])
        continue

    thing_idxs = []
    empty = True

    for j in range(N):
        if plugs[j] in things[i:]:
            thing_idx = things[i:].index(plugs[j])
        else:
            thing_idx = i
            empty = False
        
        thing_idxs.append(thing_idx)

        if not empty:
            break
    
    plug_out = thing_idxs.index(max(thing_idxs))

    del plugs[plug_out]
    plugs.append(things[i])
    cnt += 1

print(cnt)