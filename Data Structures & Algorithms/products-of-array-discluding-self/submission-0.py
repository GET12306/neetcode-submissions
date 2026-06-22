class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        count0 = 0
        for i in nums:
            pro *= i
            if i == 0:
                count0 += 1
        
        real_pro = 1
        if count0 == 1:
            
            for i in nums:
                if i != 0:
                    real_pro *= i

        
        res = [1] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                if count0 > 1:
                    res[i] = 0
                else:
                    res[i] = real_pro
            else:
                res[i] = int(pro / nums[i])
        
        return res