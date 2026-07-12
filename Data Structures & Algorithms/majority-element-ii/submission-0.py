class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        count = {}
        major_c = len(nums) // 3

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > major_c:
                res.add(num)
        return list(res)
        