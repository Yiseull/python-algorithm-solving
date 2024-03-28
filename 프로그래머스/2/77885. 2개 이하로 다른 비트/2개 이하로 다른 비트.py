def solution(numbers: list) -> list:
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            binary = list(bin(number))
            binary[1] = '0'
            for i in range(len(binary) - 1, 0, -1):
                if binary[i] == '0':
                    binary[i] = '1'
                    binary[i + 1] = '0'
                    break
            answer.append(int(''.join(binary), 2))
    
    return answer