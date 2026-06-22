class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j-i)
                if area > max_a:
                    max_a = area
        return max_a