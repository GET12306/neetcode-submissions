class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        l, r = 0, len(matrix)-1
        while l < r:
            m = l + (r-l)//2
            if matrix[m][0] > target:
                r = m-1
            elif matrix[m][0] < target:
                l = m+1
            else:
                return True
        if matrix[l][0] > target:
            l -= 1
        
        l1, r1 = 0, len(matrix[0])-1
        while l1 <= r1:
            m = l1 + (r1-l1)//2
            if matrix[l][m] > target:
                r1 = m-1
            elif matrix[l][m] < target:
                l1 = m+1
            else:
                return True
        return False