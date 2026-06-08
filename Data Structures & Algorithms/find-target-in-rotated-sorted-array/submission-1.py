class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            # Jackpot!
            if nums[middle] == target:
                return middle
                
            # Question 1: Is the LEFT half perfectly sorted?
            if nums[left] <= nums[middle]:
                # Question 2: Is the target inside this sorted boundary?
                if nums[left] <= target < nums[middle]:
                    right = middle - 1  # Target is here. Throw away the right.
                else:
                    left = middle + 1   # Target is NOT here. Throw away the left.
                    
            # Question 1 Alternative: The RIGHT half must be perfectly sorted!
            else:
                # Question 2: Is the target inside this sorted boundary?
                if nums[middle] < target <= nums[right]:
                    left = middle + 1   # Target is here. Throw away the left.
                else:
                    right = middle - 1  # Target is NOT here. Throw away the right.
                    
        return -1