def solution(phone_book) -> bool:
    phone_book.sort()
    
    for phone1, phone2 in zip(phone_book, phone_book[1:]):
        if phone2.startswith(phone1):
            return False
    
    return True