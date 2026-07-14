class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0: return
        if m==0:
            nums1[:] = nums2
            return
        
        res = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            elif nums1[p1] >= nums2[p2]:
                res.append(nums2[p2])
                p2 += 1

        if p1<m:
            for i in range(p1, m):
                res.append(nums1[i])
        if p2<n:
            for i in range(p2, n):
                res.append(nums2[i])

        for i in range(m+n):
            nums1[i] = res[i]
        