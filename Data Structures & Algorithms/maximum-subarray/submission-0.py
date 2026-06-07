class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSumSubArray = currentSum

        for i in range(1,len(nums)):
            
            currentSum = max(currentSum + nums[i], nums[i])
            maxSumSubArray = max(currentSum, maxSumSubArray)
        return maxSumSubArray


        