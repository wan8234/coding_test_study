def solution(enroll, referral, seller, amount):
    length = len(enroll)
    answer = [0] * length
    parent = {}
    key_index = {}
    
    for i in range(length):
        key_index[enroll[i]] = i
    
    for i in range(length):
        if referral[i] != '-':
            idx = enroll.index(referral[i])
            parent[enroll[i]] = idx
            
    for s in range(len(seller)):
        idx = key_index[seller[s]]
        money = amount[s] * 100
        option = money // 10
        
        answer[idx] += money - option
        
        while True:
            if enroll[idx] not in parent:
                break
            else:
                next_node = parent[enroll[idx]]
                
                money = option
                option = money // 10
                answer[next_node] += money - option
                idx = next_node
                
                if option == 0:
                    break

    return answer

# def find(parents, money, number, answer):
#     # 민호까지 돈이 들어오거나 줄 돈이 없으면 종료
#     if parents[number] == number or money // 10 == 0:
#         answer[number] += money
#         return
#     send = money // 10
#     mine = money - send
#     answer[number] += mine
#     find(parents, send, parents[number], answer)
#     return

# def solution(enroll, referral, seller, amount):
#     n = len(enroll)  # 총 사람 수(민호 포함 X)
#     answer = [0] * (n + 1)  # 민호 포함
#     d = {}  # 이름-번호의 key-value를 가지는 딕셔너리
#     parents = [i for i in range(n + 1)]  # 각자 자신을 부모로 초기화
#     # 이름-번호로 딕셔너리에 저장
#     for i in range(n):
#         d[enroll[i]] = i + 1
#     # 추천인 입력
#     for i in range(n):
#         if referral[i] == "-":  # 민호가 추천인
#             parents[i + 1] = 0
#         else:
#             parents[i + 1] = d[referral[i]]
#     # 칫솔 정산
#     for i in range(len(seller)):
#         find(parents, amount[i] * 100, d[seller[i]], answer)
#     return answer[1:]