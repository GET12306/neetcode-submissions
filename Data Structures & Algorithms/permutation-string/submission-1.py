class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        
        count_s1 = {}
        for i in s1:
            count_s1[i] = count_s1.get(i, 0) + 1

        for i in range(l2-l1+1):
            count_s2 = {}
            for j in s2[i: i+l1]:
                count_s2[j] = count_s2.get(j, 0) + 1
            if count_s2 == count_s1:
                return True
        return False