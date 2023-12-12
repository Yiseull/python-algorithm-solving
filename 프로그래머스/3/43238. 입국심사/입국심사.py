def solution(n, times) -> int:
    start, end = 1, n * max(times)
    
    while start < end:
        mid = (start + end) // 2
        
        cnt = 0
        for time in times:
            cnt += mid // time
            
        if cnt < n:
            start = mid + 1
        else:
            end = mid
        
    return start