class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_list = set()

        sorted_list = sorted(nums)
        for i in range(len(nums)):
            target = -sorted_list[i]
            p1, p2 = i+1, len(nums) - 1
            while p1 < p2:
                if p1 == i:
                    p1 += 1
                if p2 == i:
                    p2 -= 1
                cur = sorted_list[p1] + sorted_list[p2]
                if cur == target:
                    ans_list.add((sorted_list[i], sorted_list[p1], sorted_list[p2]))
                    p1 += 1
                    p2 -= 1
                elif cur < target:
                    p1 += 1
                else:
                    p2 -= 1

        return [list(i) for i in ans_list]