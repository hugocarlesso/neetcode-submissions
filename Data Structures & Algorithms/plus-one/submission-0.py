class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Brut force
        total = 1
        digits.reverse()
        for i,digit in enumerate(digits):
            total += 10**i * digit
        result = []
        while total > 0:
            result.append(total%10)
            total //=10
        result.reverse()
        return result