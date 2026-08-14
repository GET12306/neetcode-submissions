class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        res = 0

        while p1 < p2:
            cur = (p2 - p1) * min(heights[p1], heights[p2])
            res = max(res, cur)
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1

        return res
