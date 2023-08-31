def make_correct_parentheses(w):
    # 입력이 빈 문자열인 경우, 빈 문자열 반환
    if w == '':
        return w
    
    left, right = 0, 0
    u, v = '', ''
    stack = []
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
            stack.append(w[i])
        else:
            right += 1
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(w[i])
                
        # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
        if left == right:
            u = w[:i + 1]
            v = w[i + 1:]
            break
            
    # 문자열 u가 "올바른 괄호 문자열"이 아니라면
    if stack:
        #  빈 문자열에 '(' + '문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열' + ')'를 붙임
        s = '(' + make_correct_parentheses(v) + ')'
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙임
        tmp = ''
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                tmp += ')'
            else:
                tmp += '('
                
        return s + tmp
    
    # 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행
    return u + make_correct_parentheses(v)
            

def solution(p):
    return make_correct_parentheses(p)