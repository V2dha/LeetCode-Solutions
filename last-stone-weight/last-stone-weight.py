import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if not stones:
            return 0
        heapq.heapify(stones)
        while len(stones) > 1:
            y, x = heapq.nlargest(2, stones)
            if x != y:
                heapq.heappush(stones, y-x)
            stones.remove(x)
            stones.remove(y)
            print(stones)
        if not stones:
            return 0
        else:
            return stones[0]