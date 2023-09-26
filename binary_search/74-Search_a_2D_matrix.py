class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binSearch(lst, t):
            l, r = 0, len(lst) - 1

            while l <= r:
                mid = l + ((r - l) // 2)
                if lst[mid] < t:
                    l = mid + 1
                elif lst[mid] > t:
                    r = mid -1
                else:
                    return True
            return False
        
        lRow, rRow = 0, len(matrix) - 1
        while lRow <= rRow:
            mRow = lRow + ((rRow - lRow) // 2)
            found = binSearch(matrix[mRow], target)

            if not found and matrix[mRow][0] < target:
                lRow = mRow + 1
            elif not found and matrix[mRow][-1] > target:
                rRow = mRow - 1
            else:
                return found
        return False