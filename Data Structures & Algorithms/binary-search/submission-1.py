class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we will split nums in half 
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2

        while left < right:

            if target <= nums[middle]:
                right = middle
            else:
                left = middle + 1 
            middle = middle = (left + right) // 2
        return left if target == nums[left] else -1
        