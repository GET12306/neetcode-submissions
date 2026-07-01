class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)

        mlen = 0

        for num in nums:
            if num-1 not in nset:
                tlen = 0
                while num in nset:
                    tlen += 1
                    num += 1
                mlen = max(mlen, tlen)
        
        return mlen

