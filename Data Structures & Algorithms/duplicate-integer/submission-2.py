class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 3]
    ss = Solution()
    print(ss.hasDuplicate(nums))
