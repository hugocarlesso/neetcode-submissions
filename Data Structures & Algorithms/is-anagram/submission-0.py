class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occ1 = {}
        for car in s:
            occ1[car] =  occ1.get(car,0) +1

        occ2 = {}
        for car in t:
            if car not in occ1:
                return False
            occ2[car] =  occ2.get(car,0) +1
        return occ1 == occ2