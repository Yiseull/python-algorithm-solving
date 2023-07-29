def solution(s):
    stack = []
    
    for alpha in s:
        if stack and stack[-1] == alpha:
            stack.pop()
        else:
            stack.append(alpha)
        
    return 0 if stack else 1