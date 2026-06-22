class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

if __name__ == "__main__":
    nums = [4, 5, 6]
    tar = 10
    solution = Solution()
    result = solution.twoSum(nums, tar)
    print(result)
