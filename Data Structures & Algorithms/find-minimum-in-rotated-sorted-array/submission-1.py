class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        globalMin = min(nums[left], nums[right])
        while nums[left] > nums[right]:
            middle = (left + right) // 2
            if nums[middle] > nums[left]:
                left = middle
                globalMin = min(nums[left], globalMin)
            else:
                right = middle
                globalMin = min(nums[right], globalMin)
        return globalMin
            
        