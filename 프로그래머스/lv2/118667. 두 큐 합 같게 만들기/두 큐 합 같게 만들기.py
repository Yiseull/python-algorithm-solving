from collections import deque


def solution(queue1, queue2) -> int:
    nm = len(queue1) * 2 + len(queue2) * 2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    count = 0
    
    while sum1 != sum2:
        count += 1
        if count > nm:
            return -1
        
        if sum1 > sum2:
            e = queue1.popleft()
            sum1 -= e
            sum2 += e
            queue2.append(e)
        else:
            e = queue2.popleft()
            sum1 += e
            sum2 -= e
            queue1.append(e)
            
    return count