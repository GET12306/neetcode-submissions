class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k >= n: return arr
        if x >= arr[-1]: return arr[-k:]
        if x <= arr[0]: return arr[:k]

        l, r = 0, len(arr)-1
        while r-l+1 > k:
            disl = x-arr[l]
            disr = arr[r]-x
            if disl <= disr:
                r -= 1
            else:
                l += 1

        return arr[l:r+1]