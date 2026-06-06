class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # count.items() gives us tuples like (number, frequency)
        # We sort by frequency (index 1), in descending order
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Extract just the numbers (index 0) from the top k items
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
            
        return result


        
