def compress(unit, s) -> str:
    compressed_s = ''
    count = 1
    tmp_s = s[:unit]
    
    for i in range(unit, len(s), unit):
        cur_s = s[i:i+unit]
        if tmp_s == cur_s:
            count += 1
        elif count == 1:
            compressed_s += tmp_s
            tmp_s = cur_s
        else:
            compressed_s += str(count) + tmp_s
            tmp_s = cur_s
            count = 1
            
    if count == 1:
        compressed_s += tmp_s
    else:
        compressed_s += str(count) + tmp_s
        
    return compressed_s
    

def solution(s) -> int:
    if len(s) == 1:
        return 1
    
    answer = 1000
    
    for i in range(1, len(s) // 2 + 1):
        compressed_s = compress(i, s)
        answer = min(answer, len(compressed_s))
        
    return answer