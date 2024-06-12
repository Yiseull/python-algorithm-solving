def solution(n: int, arr1: list, arr2: list) -> list:
    answer = [''] * n
    for i in range(n):
        answer[i] = bin(arr1[i]|arr2[i])[2:].zfill(n).replace('1', '#').replace('0', ' ')
            
    return answer