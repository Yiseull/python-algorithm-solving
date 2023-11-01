def solution(s):
    i = 0
    answer = ''
    for c in s:
        if c.isalpha():
            if i % 2 == 0:
                c = c.upper()
            else:
                c = c.lower()
            i += 1
        else:
            i = 0
        answer += c
    
    return answer