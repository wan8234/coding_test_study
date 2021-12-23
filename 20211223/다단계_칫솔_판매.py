def solution(enroll, referral, seller, amount):
    answer = []
    R = dict()
    M = dict()

    for i in range(len(enroll)):
        R[enroll[i]] = referral[i]
        M[enroll[i]] = 0

    def referfee(e, money):
        if money == 0:
            return
        fee = int(money * 0.1)
        M[e] += money - fee
        if R[e] != "-":
            referfee(R[e], fee)

    for i in range(len(seller)):
        referfee(seller[i], amount[i] * 100)

    for i in range(len(enroll)):
        answer.append(M[enroll[i]])

    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10])