class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 최솟값을 구해서 피벗으로 설정
        pivot:int = nums.index(min(nums))
            
        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid: int = (left + right) // 2
            mid_pivot: int = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        
        return -1