def solution(n) -> int:
    answer = 0
    
    while n:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            answer += 1
        
    return answer