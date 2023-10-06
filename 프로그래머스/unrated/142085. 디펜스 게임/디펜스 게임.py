from heapq import *


def solution(n, k, enemy):
    answer = 0
    q = []
    
    for e in enemy:
        heappush(q, e)
        
        while len(q) > k:
            n -= heappop(q)
            if n < 0:
                return answer
                
        answer += 1
    
    return answer