class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def digits(n:int):
            resu = []
            while n > 0:
                resu.append(n%10)
                n //= 10
            return resu
        while n not in seen and n !=1:
            seen.add(n)
            digitsList = digits(n)
            sumSquarred = 0
            for digit in digitsList:
                sumSquarred += digit **2
            n = sumSquarred
        return n == 1 

        