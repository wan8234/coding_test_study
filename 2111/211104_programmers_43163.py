#### USING DFS ####

answer = 0
def solution(begin, target, words):
    global answer
    answer = int(1e9)
    visit = [0] * len(words)
    
    if target not in words:
        return 0
    
    dfs(begin, target, 0, visit, words)
    
    return answer

def dfs(word, target, count, visit, words):
    global answer
    
    if word == target:
        answer = min(count, answer)
        return
    
    length = len(visit)
    
    for w in range(length):
        if visit[w] == 0:
            compare = check(word, words[w])
            if compare == 1:
                visit[w] = 1
                dfs(words[w], target, count + 1, visit, words)
                visit[w] = 0
                
def check(first, second):
    length = len(first)
    count = 0
    
    for i in range(length):
        if first[i] != second[i]:
            count += 1
    return count


#### USING GENERATOR ####

from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word): # zip은 리스트를 쌍으로 묶어줌
            if c != w:
                count += 1

        if count == 1:
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)