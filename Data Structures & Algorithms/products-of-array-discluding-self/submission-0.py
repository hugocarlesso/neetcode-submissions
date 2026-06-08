class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = [0] * len(nums)
        totalZeroes = 0
        indexZero = 0
        for i,num in enumerate(nums):
            if num == 0:
                # We count the number of 0 in nums
                totalZeroes += 1
                # We keep the index of where there is a 0
                indexZero = i
                # If there was more than only one zero everything is 0
                if totalZeroes > 1 :
                    return [0] * len(nums)
            else:
                product*= num
        for i, num in enumerate(nums):
            if totalZeroes>0:
                if i != indexZero:
                    result[i] = 0
                else:
                    result[i] = product
            else:
                result[i] = product // num
        return result
            
        
        

        
        

                
        
        

"""

Probleme with 0


"""
        