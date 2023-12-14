def solution(phone_book) -> bool:
    phone_book.sort()
    
    for phone1, phone2 in zip(phone_book, phone_book[1:]):
        if phone1 == phone2[:len(phone1)]:
            return False
    
    return True