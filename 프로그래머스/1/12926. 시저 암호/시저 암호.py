def solution(s, n):
    answer = ''
    
    for c in s:
        if c.isalpha():
            c = ord(c)
            if (64 < c < 91 and c + n > 90) or (c > 96 and c + n > 122):
                c -= 26
            c = chr(c + n)
            
        answer += c
        
    return answer