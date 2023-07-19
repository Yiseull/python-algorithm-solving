def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
            continue
            
        elif not stack or stack[-1] != '(':
            return False
        
        stack.pop()
    
    return not stack