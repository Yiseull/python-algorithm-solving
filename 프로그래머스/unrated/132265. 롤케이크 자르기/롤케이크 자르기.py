from collections import Counter, defaultdict


def solution(topping) -> int:
    answer = 0
    left, right = defaultdict(int), Counter(topping)
    left_topping_size, right_topping_size = 0, len(right)
    
    for t in topping:
        left[t] += 1
        right[t] -= 1
        
        if left[t] == 1:
            left_topping_size += 1
        
        if right[t] == 0:
            right_topping_size -= 1
        
        if left_topping_size == right_topping_size:
            answer += 1
            
    return answer