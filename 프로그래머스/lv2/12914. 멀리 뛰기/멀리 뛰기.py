def solution(n):
    a, b = 1, 2
    
    for i in range(n - 1):
        a, b = b, a + b
        
    return a % 1234567