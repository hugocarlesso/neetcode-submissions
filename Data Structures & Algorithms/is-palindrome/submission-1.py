class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip bad characters on the left side
            while left < right and not s[left].isalnum():
                left += 1
                
            # Skip bad characters on the right side
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Both pointers are now on valid characters! Compare them.
            if s[left].lower() != s[right].lower():
                return False
                
            # Move both pointers inward for the next check
            left += 1
            right -= 1
            
        return True