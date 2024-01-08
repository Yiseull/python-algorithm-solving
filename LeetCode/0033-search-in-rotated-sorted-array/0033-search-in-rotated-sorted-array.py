class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = nums.index(min(nums))
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            pivot_mid = (mid + pivot) % n
            
            if nums[pivot_mid] < target:
                left = mid + 1
            elif nums[pivot_mid] > target:
                right = mid - 1
            else:
                return pivot_mid
            
        return -1