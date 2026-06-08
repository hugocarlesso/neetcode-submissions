class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1
        
        keys = list(count.keys())
        keys.sort(key= lambda x: count[x], reverse = True)

        return keys[:k]
        
