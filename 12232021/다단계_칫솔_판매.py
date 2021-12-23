def solution(enroll, referral, seller, amount):
    answer = []

    for i in range(0,len(enroll)) :
        answer.append(0)
    for i in range(0,len(amount)) :
        amount[i] *= 100
    for i in range(0,len(seller)) :
        person = seller[i]
        money = amount[i]

        while True :
            if person == '-' : break
            nextMoney = money//10
            money = money - nextMoney
            i = enroll.index(person)
            answer[i] += money

            if nextMoney != 0 : 
                person = referral[i]
                money = nextMoney
            else : break

    return answer
