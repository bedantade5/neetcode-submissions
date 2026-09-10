class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l, r = 0, (r*c)-1
        while l <= r:
            mid = (l+r)//2
            row = mid//c
            col = mid%c
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        return False