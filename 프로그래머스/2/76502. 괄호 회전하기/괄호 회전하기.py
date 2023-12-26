def solution(s) -> int:
    answer = 0
    
    for i in range(len(s)):
        stack = []
        copy_s = s[i:] + s[:i]
        
        for c in copy_s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif stack:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
            else:
                stack.append(0)
                break
                
        if not stack:
            answer += 1
            
    return answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     stack = []
#     for i in s:
#         if i == '(' or i == '[' or i == '{':
#             stack.append(i)
#         elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
#             stack.pop()
#         else:
#             return False
#     return False if stack else True


# def solution(s) -> int:
#     answer = 0
#     for x in range(len(s)):
#         s_copy = s[x:] + s[:x]
#         if check(s_copy):
#             answer += 1
    
#     return answer