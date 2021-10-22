# 16진수 적힌 보물상자
# 상자의 뚜껑은 시계 방향으로 돌릴 수 있음
# 회전 시 숫자가 한칸씩 시계 방향으로 회전
# 각 변에는 동일한 개수의 숫자
# 시계 방향 순으로 높은 자리 숫자에 해당, 하나의 수 가리킴
# 보물 상자에는 자물쇠 걸려 있음
# 비밀 번호는 보물상자에 적힌 숫자로 만들 수 있는 모든 수 중 K번째로 큰 수를 10진 수로 만든 수
# N개의 숫자가 입력으로 주어졌을 때, 보물상자의 비밀번호를 출력하는 프로그램 만들기
# 같은 수를 중복으로 세지 않도록 주의

def solve(lock):
    number = []
    series = []
    interval = len(lock) // 4

    for i in range(interval):
        for j in range(4):
            temp = lock[j * interval : j * interval + interval]
            if temp not in number:
                number.append(temp)
        
        lock = lock[-1] + lock[:len(lock) - 1]
    
    for num in number:
        series.append(change(num, interval))

    series.sort(reverse=True)

    return series[K - 1]
    
def change(string, interval):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    number = 0
    six = 16**(interval - 1)

    for s in string:
        if s in alpha:
            temp = ord(s) - ord('A') + 10
            number += temp * six
        else:
            number += int(s) * six
        
        six //= 16
    
    return number    

T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, K = map(int, input().split())
    lock = input()

    result = solve(lock)

    print('#{} {}'.format(test_case, result))

# 5
# 12 10
# 1B3B3B81F75E
# 16 2
# F53586D76286B2D8
# 20 14
# 88F611AE414A751A767B
# 24 16
# 044D3EBA6A647B2567A91D0E
# 28 11
# 8E0B7DD258D4122317E3ADBFEA99