import heapq

def solution(operations):
    answer = []
    
    heap_queue = list()  
    
    for i in range(len(operations)):
        
        oper,num = operations[i].split()
        
        if oper == 'I':
            
            heapq.heappush(heap_queue,int(num))   
            
        elif oper == 'D':
            
            if heap_queue:
                
                if int(num) == -1:
                
                    heapq.heappop(heap_queue)
                
                else:
                    
                    heap_queue = heapq.nlargest(len(heap_queue),heap_queue)[1:]
                    heapq.heapify(heap_queue)
            else:
                pass
                
                            
    if heap_queue:
        #answer = [heap_queue[-1],heap_queue[0]]
        answer = [heapq.nlargest(1,heap_queue)[0],heapq.nsmallest(1,heap_queue)[0]]
    else:
        answer = [0,0]
            
        
    return answer