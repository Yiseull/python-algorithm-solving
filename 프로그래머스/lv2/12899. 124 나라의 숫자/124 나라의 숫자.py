def solution(n):
    answer = ''
    while n > 0:
        remain = n % 3
        n //= 3
        if remain == 0:
            answer += str(4)
            n -= 1
        else:
            answer += str(remain)
        
    return answer[::-1]