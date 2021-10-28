def solution(jobs):
    answer = 0
    jobs = sorted(jobs, key=lambda x: x[1])
    time = 0
    while jobs:
        for i in len(jobs):
            if jobs[i][0] <= time:
                time += jobs[i][1]
                answer += time - jobs[i][0]
                break
        else:
            time += 1
            
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))