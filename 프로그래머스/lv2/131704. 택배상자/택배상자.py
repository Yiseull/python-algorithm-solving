def solution(order):
    answer = 0
    stack = []
    cur, i = 1, 0
    while cur < len(order) + 1:
        if cur == order[i]:
            answer += 1
            i += 1
        else:
            stack.append(cur)
        cur += 1
        
        while (stack and stack[-1] == order[i]):
            stack.pop()
            answer += 1
            i += 1

    return answer