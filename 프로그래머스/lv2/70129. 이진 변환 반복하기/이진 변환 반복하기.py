def solution(s):
    answer = [0, 0]

    while s != '1':
        c = s.count('1')
        
        answer[0] += 1
        answer[1] += len(s) - c
        
        s = bin(c)[2:]

    return answer