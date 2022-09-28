# import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ x * (-1) for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if first != second:
                heapq.heappush(stones, first - second)
        
        return -stones[0] if len(stones) else 0