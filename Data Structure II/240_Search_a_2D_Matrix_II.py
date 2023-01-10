class Solution:
    def BSearch(self, arr, targ):
        l, r = 0, len(arr)-1
        mid = int(l + ((r-l)/2))
        ans = False
        
        while l <= r:
            mid = int(l + ((r-l)/2))
            if targ == arr[mid]:
                ans = True
                break
            elif arr[mid] < targ:
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0
        Nr, Nc = len(matrix[0]), len(matrix)
        ele = matrix[i][j]
        ans = False
        
        # check if the target exists in any Row of matrix by applying Binary Search
        for r in matrix:
            ans = self.BSearch(r, target)
            if ans:
                break

        return ans