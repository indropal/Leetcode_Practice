class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        ans = [[0 for _ in range(n)] for _ in range(n)]; # print(ans)
        startLim, endLim = 0, n-1
        cnt = 1

        while startLim <= endLim:
            
            if startLim == endLim:
                # Referencing the center element
                ans[startLim+i][endLim+i] = cnt
                break
            
            # traverse over the entire outer boundary-layer of the matrix
            # the path will be starting from 'startLim' row
            # - 'startLim' row from 'startlim' till 'endlim' elements
            # - 'endlim' column from 'startLim+1' till 'endLim' elements
            # - 'endlim' row from 'endlim-1' till 'startLim' elements
            # - 'startLim' column from 'endlim-1' till 'startLim-1'

            numIter, i = endLim - startLim, startLim

            while 0 < numIter:
                # iterate the startLim row
                ans[startLim][i] = cnt
                i += 1
                cnt += 1
                numIter -= 1

            numIter, i = endLim - startLim, startLim
            while 0 < numIter:
                # iterate the endLim column
                ans[i][endLim] = cnt
                cnt += 1
                i += 1
                numIter -= 1
            
            numIter, i = endLim - startLim, endLim
            while 0 < numIter:
                # iterate the endLim row
                ans[endLim][i] = cnt
                cnt += 1
                i -= 1
                numIter -= 1
            
            numIter, i = endLim - startLim, endLim
            while 0 < numIter:
                # iterate the startLim column
                ans[i][startLim] = cnt
                cnt += 1
                i -= 1
                numIter -= 1

            startLim += 1
            endLim -= 1
            i = 0

        return ans