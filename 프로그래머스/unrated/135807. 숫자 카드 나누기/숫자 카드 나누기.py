from math import gcd


def check_condition(a, array) -> int:
    for x in array:
        if x % a == 0:
            return 0
    return a


def calculate_all_gcd(array, n) -> int:
    a = max(1, gcd(array[0], array[1]))
    for i in range(2, n):
        a = gcd(a, array[i])
    return a
    

def solution(arrayA, arrayB) -> int:
    n = len(arrayA)
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    if n != 1:
        gcdA = calculate_all_gcd(arrayA, n)
        gcdB = calculate_all_gcd(arrayB, n)
    return max(check_condition(gcdA, arrayB), check_condition(gcdB, arrayA))
