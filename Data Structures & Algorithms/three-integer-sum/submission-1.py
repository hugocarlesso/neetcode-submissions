class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort the array so we can use Two Pointers and easily skip duplicates
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # If the current number is greater than 0, we can stop. 
            # Three positive numbers can never add up to 0!
            if nums[i] > 0:
                break
                
            # Skip duplicates for our "locked" first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Now, it is just standard Two Sum II !
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    # We found a match!
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers inward
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the left pointer to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return result