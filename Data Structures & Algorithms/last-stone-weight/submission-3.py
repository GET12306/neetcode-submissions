class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        a = [-x for x in stones]
        heapq.heapify(a)

        while len(a) > 1:
            first = heapq.heappop(a)
            second = heapq.heappop(a)

            if first != second:
                heapq.heappush(a, -1 * abs(first-second))
        
        a.append(0)

        return a[0] * -1
