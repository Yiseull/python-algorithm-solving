def solution(n: int, s: int) -> list:
    if s < n:
        return [-1]
    
    answer = []
    i = n
    for _ in range(n):
        answer.append(s // i)
        s -= s // i
        i -= 1
        
    return answer