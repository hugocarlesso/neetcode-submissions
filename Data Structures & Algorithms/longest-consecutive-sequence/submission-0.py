class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        for start in nums:
            currentLength = 1
            while start + 1 in nums:
                currentLength += 1 
                start += 1
            maxLength = max(currentLength, maxLength)
        return maxLength