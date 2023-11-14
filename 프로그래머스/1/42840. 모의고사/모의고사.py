def solution(answers) -> list:
    result = [0, 0, 0]
    
    student1 = [1, 2, 3, 4, 5] 
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, student in enumerate([student1, student2, student3]):
        idx = 0
        n = len(student)
        for answer in answers:
            if student[idx] == answer:
                result[i] += 1
            idx = (idx + 1) % n
    
    return [i + 1 for i in range(3) if result[i] == max(result)]