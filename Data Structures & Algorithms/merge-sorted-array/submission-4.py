class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2
            return

        res = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1

        res.extend(nums1[p1:m])
        res.extend(nums2[p2:n])

        nums1[:] = res
