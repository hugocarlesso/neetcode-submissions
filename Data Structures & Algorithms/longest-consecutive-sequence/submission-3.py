class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        maxLength = 0
        for start in numsSet:
            # we start counting only if this is the start of a sequence
            if start - 1 not in numsSet:
                currentNum = start
                currentLength = 1
                while currentNum +1 in numsSet:
                    currentLength +=1
                    currentNum += 1
                maxLength = max(maxLength, currentLength)
        return maxLength    

"""
--------------------
nums = [0,3,2,5,4,6,1,1]

seen = 

"""