class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = ""
        for i in digits:
            num_str += str(i)
        num = int(num_str)
        num += 1
        num_1_str = str(num)
        result = []
        for i in num_1_str:
            result.append(i)
        return result