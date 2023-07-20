def solution(n):
    answer = 0
    numbers = [i for i in range(1, n + 1)]
    start, end = 0, 0
    sum = 1
    
    while end < n - 1:
        if sum > n:
            sum -= numbers[start]
            start += 1
        else:
            if sum == n:
                answer += 1
            end += 1
            sum += numbers[end]
            
    return answer + 1