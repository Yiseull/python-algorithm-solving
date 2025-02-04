def solution(sequence: list, k: int) -> list:
    answer = [0, 1000000, 1000000]
    length = len(sequence)
    left, right = 0, 0
    total = sequence[0]
    
    while left <= right:
        if total < k and right < length - 1:
            right += 1
            total += sequence[right]
            continue
        
        if total == k and answer[2] > right - left:
            answer = [left, right, right - left]
        
        total -= sequence[left]
        left += 1
    
    return answer[:2]


# def solution(sequence, k) -> list:
#     answer = [0, 0]
#     start, end = 0, 0
#     total, size = sequence[0], 1000000
#     n = len(sequence)
    
#     while 1:
#         if total > k:
#             total -= sequence[start]
#             start += 1
#             continue
        
#         if total == k and (end - start) < size:
#                 size = end - start
#                 answer = [start, end]
                
#         end += 1
#         if end == n:
#             break
#         total += sequence[end]
    
#     return answer