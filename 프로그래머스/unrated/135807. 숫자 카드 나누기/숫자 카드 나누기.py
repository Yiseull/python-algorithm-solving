def check_condition(gcd, array) -> int:
    for x in array:
        if x % gcd == 0:
            return 0
    return gcd


def calculate_gcd(a, b) -> int:
    while b:
        a, b = b, a % b
    return a


def calculate_all_gcd(array, n) -> int:
    gcd = max(1, calculate_gcd(array[0], array[1]))
    for i in range(2, n):
        gcd = calculate_gcd(gcd, array[i])
    return gcd
    

def solution(arrayA, arrayB) -> int:
    n = len(arrayA)
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    if n != 1:
        gcdA = calculate_all_gcd(arrayA, n)
        gcdB = calculate_all_gcd(arrayB, n)
    return max(check_condition(gcdA, arrayB), check_condition(gcdB, arrayA))
