class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] < nums[-1]:
            return self.bi_search(nums, left=0, right=len(nums)-1, target=target)
        
        p1, p2 = 0, len(nums)-1
        while p1 < p2:
            m = p1 + (p2-p1) // 2
            if nums[m] > nums[p2]:
                p1 = m + 1
            else:
                p2 = m

        result = self.bi_search(nums, left=0, right=p1-1, target=target)
        if result != -1:
            return result
        else:
            return self.bi_search(nums, p1, len(nums)-1, target)

    
    def bi_search(self, nums_p, left, right, target) -> int:
        p1, p2 = left, right
        while p1 <= p2:
            m = p1 + (p2-p1) // 2
            if nums_p[m] > target:
                p2 = m - 1
            elif nums_p[m] < target:
                p1 = m + 1
            else:
                return m
        return -1