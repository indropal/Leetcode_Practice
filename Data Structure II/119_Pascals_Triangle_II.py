class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        if rowIndex == 2:
            return [1, 2, 1]
        
        tmp, dp = [1, 2, 1], []
        rowIndex -= 2

        while 0 < rowIndex:
            idx, N = 0, len(tmp)
            dp = []

            while idx + 1 < N:
                dp.append(tmp[idx] + tmp[idx+1])
                idx += 1

            dp.append(1)
            dp.insert(0, 1); #print(dp)

            tmp = dp
            rowIndex -= 1
    
        return dp

