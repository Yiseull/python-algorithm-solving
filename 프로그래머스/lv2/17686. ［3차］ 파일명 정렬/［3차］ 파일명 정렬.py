def solution(files):
    files_list = []
    
    for file in files:
        head, number = '', ''
        digit_start, digit_end = 1000, 1000
        
        for i, char in enumerate(file):
            # NUMBER 시작 (처음 숫자가 나올 때)
            if digit_start == 1000 and char.isdigit():
                head = file[:i]
                digit_start = i
            # NUMBER 끝난 다음 문자
            elif digit_start != 1000 and digit_end == 1000 and not char.isdigit():
                digit_end = i
                number = file[digit_start:digit_end]    
                break
                
        # NUMBER로 끝나는 경우
        if not number:
            digit_end = len(file)
            number = file[digit_start:digit_end]    
            
        files_list.append([head, number, file[digit_end:]])
    
    files_list.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return  [''.join(file_list) for file_list in files_list]