def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    island = set([costs[0][0]])
    res = 0
    
    while len(island) != n:
        for c in costs:
            # 닫히게 되면 무시
            if c[0] in island and c[1] in island:
                continue
            elif c[0] in island or c[1] in island:
                island.update([c[0],c[1]])
                res += c[2]
                break
    return res
