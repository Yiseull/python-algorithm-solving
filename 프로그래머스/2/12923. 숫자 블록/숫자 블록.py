from math import sqrt


def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
            
        num = 1
        for tmp in range(2, int(sqrt(i) + 1)):
            if i % tmp == 0:
                if i // tmp <= 10000000:
                    num = i // tmp
                    break
                else:
                    num = tmp
        answer.append(num)
            
    return answer