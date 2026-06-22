class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, value in enumerate(nums):
            if value not in nums[:i]:
                continue
            else:
                return True
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 3]
    ss = Solution()
    print(ss.hasDuplicate(nums))
