def solution(s):
    for c in s:
        if c.isalpha():
            return False
        
    return len(s) == 4 or len(s) == 6