def solution(numbers):
    global answer
    answer = 0
    global array
    array = [0] * len(numbers)
    global exist
    exist = []
    
    def sosu(numbers, current):
        global answer
        global array
        global exist
        
        for i in range(len(numbers)):            
            if array[i] != 1:
                array[i] = 1
                temp = current + numbers[i]                
                        
                sosu(numbers, temp)
                array[i] = 0
                
                temp = int(temp)
                if temp in exist:
                    continue
                else:
                    exist.append(temp)                
                
                count = 0
                if temp == 2:
                    answer += 1
                elif temp == 3:
                    answer += 1
                elif temp > 3:
                    for j in range(1, temp//2 + 1):
                        if temp % j == 0:
                            count += 1
                    if count == 1:
                        answer += 1                   
        
    sosu(numbers, '')
    
    return answer