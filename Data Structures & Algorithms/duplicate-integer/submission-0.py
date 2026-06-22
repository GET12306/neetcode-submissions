class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        known = []
        for i in nums:
            if i not in known:
                known.append(i)
            else:
                return True
        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 3]
    ss = Solution()
    print(ss.hasDuplicate(nums))
