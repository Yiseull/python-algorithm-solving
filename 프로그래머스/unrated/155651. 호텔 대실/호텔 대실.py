from heapq import *
CLEANING_TIME = 10

def solution(book_time):
    # 시각을 숫자로 변환
    for i, bt in enumerate(book_time):
        start = int(bt[0][:2]) * 60 + int(bt[0][3:])
        end = int(bt[1][:2]) * 60 + int(bt[1][3:])
        book_time[i] = [start, end]
        
    book_time.sort()
    
    required_room_count = 0 # 필요한 객실의 수
    heap = [] # 사용 중인 방의 퇴실 시각 리스트
    for start, end in book_time:
        while heap and start >= heap[0] + CLEANING_TIME:
            heappop(heap)
        
        if required_room_count == len(heap):
            required_room_count += 1
        heappush(heap, end)
        
    return required_room_count