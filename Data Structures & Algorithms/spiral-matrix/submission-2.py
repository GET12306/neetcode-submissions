class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        all_elements = rows * cols
        preleft, preright, preup, predown = 0, cols-1, 1, rows-1
        
        go_dic = 'right'
        cur_r, cur_c = 0, 0
        res.append(matrix[0][0])

        while len(res) < all_elements:
            if go_dic == 'right':
                for i in range(cur_c+1, preright+1):
                    res.append(matrix[cur_r][i])
                cur_c = preright
                preright -= 1
                go_dic = 'down'
            elif go_dic == 'down':
                for i in range(cur_r+1, predown+1):
                    res.append(matrix[i][cur_c])
                cur_r = predown
                predown -= 1
                go_dic = 'left'
            elif go_dic == 'left':
                for i in range(cur_c-1, preleft-1, -1):
                    res.append(matrix[cur_r][i])
                cur_c = preleft
                preleft += 1
                go_dic = 'up'
            elif go_dic == 'up':
                for i in range(cur_r-1, preup-1, -1):
                    res.append(matrix[i][cur_c])
                cur_r = preup
                preup += 1
                go_dic = 'right'
            
        return res