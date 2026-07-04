class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // len(matrix[0]) if len(matrix) > 1 else 0
            col = mid % len(matrix[0])
            print(l, r, mid, row, col)
            # if row < len(matrix) and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
            # else:
            #     break
        return False

        