class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            cur_longest = 0
            if num-1 not in numset:
                cur_longest = 1
                next_num = num + 1
                while next_num in numset:
                    cur_longest += 1
                    next_num += 1
            longest = max(longest, cur_longest)
            
        return longest