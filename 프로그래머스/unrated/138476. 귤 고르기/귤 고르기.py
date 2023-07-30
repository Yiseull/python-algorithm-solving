from collections import Counter


def solution(k, tangerine):
    answer = 0
    total = 0
    
    for size, cnt in Counter(tangerine).most_common():
        total += cnt
        answer += 1
        
        if total >= k:
            break
            
    return answer