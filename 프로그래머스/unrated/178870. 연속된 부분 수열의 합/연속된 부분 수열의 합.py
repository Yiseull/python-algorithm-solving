def solution(sequence, k) -> list:
    answer = [0, 0]
    start, end = 0, 0
    total, size = sequence[0], 1000000
    n = len(sequence)
    
    while 1:
        if total > k:
            total -= sequence[start]
            start += 1
            continue
        
        if total == k and (end - start) < size:
                size = end - start
                answer = [start, end]
                
        end += 1
        if end == n:
            break
        total += sequence[end]
    
    return answer