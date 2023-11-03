def base10_to_base3(n) -> str:
    num = ''
    while n > 0:
        num += str(n % 3)
        n //= 3
    return num


def base3_to_base10(n) -> int:
    num = 0
    p = 1
    for i in range(len(n) - 1, -1, -1):
        num += int(n[i]) * p
        p *= 3
    return num
    

def solution(n):
    return base3_to_base10(base10_to_base3(n))