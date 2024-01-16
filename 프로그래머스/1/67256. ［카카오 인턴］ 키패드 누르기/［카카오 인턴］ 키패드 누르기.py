def solution(numbers: list, hand: str) -> str:
    answer = ''
    left, right = 10, 12
    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            left = number
        elif number in (3, 6, 9):
            answer += 'R'
            right = number
        else:
            if number == 0:
                number = 11
            l = abs(number - left)
            l = l % 3 + l // 3
            r = abs(number - right)
            r = r % 3 + r // 3
            if l < r:
                answer += 'L'
                left = number
            elif l > r:              
                answer += 'R'
                right = number
            elif hand == 'right':            
                answer += 'R'
                right = number
            else:
                answer += 'L'
                left = number
    
    return answer