class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        cur = numbers[p1] + numbers[p2]
        while cur != target:
            if cur < target:
                p1 += 1
            else:
                p2 -= 1
            cur = numbers[p1] + numbers[p2]
        return [p1+1, p2+1]
