class Solution:
    def isPalindrome(self, s: str) -> bool:
        changed_s: str = ''

        for char in s:
            if char.isalnum():
                changed_s += char.lower()
        
        return changed_s == changed_s[::-1]