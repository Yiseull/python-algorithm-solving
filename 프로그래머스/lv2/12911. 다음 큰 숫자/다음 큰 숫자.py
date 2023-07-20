def solution(n):
    n_binary_one_count = bin(n).count('1')
    number = n + 1
    while 1:
        if n_binary_one_count == bin(number).count('1'):
            break
        number += 1
            
    return number