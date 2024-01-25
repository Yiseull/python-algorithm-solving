from math import sqrt


def is_prime_number(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
    

def make_base_k(n: int, k: int) -> str:
    base_k = ''
    while n > 0:
        base_k += str(n % k)
        n //= k
    return base_k[::-1]


def solution(n: int, k: int) -> int:
    answer = 0
    base_k = make_base_k(n, k)
    for n in base_k.split('0'):
        if n.isdigit() and is_prime_number(int(n)):
            answer += 1
    
    return answer