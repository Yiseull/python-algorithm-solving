def solution(n):
    n_binary_one_count = bin(n).count('1')
    while 1:
        n += 1
        if n_binary_one_count == bin(n).count('1'):
            break
            
    return n