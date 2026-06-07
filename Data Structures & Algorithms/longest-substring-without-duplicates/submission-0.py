class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        
        # 'right' is our incoming character
        for right in range(len(s)):
            
            # If the incoming character is already in our window...
            # We MUST shrink the window from the left until the duplicate is gone!
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Now that it's safe, add the new character to the set
            char_set.add(s[right])
            
            # Did this new valid window beat our high score?
            max_len = max(max_len, right - left + 1)
            
        return max_len