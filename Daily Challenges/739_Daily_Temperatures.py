class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        N = len(temperatures)
        waitArr = [0 for _ in range(N)]
        
        """
        # BRUTE FORCE Technique ~ get TLE
        for idx in range(N):
            
            if idx == N-1:
                waitArr[idx] = 0
                break
            
            tIdx = idx+1 #; print(idx, temperatures[idx])

            while (tIdx <= N-1) and ( temperatures[tIdx] <= temperatures[idx]):
                tIdx += 1

            if (tIdx <= N-1) and (temperatures[idx] < temperatures[tIdx]):
                waitArr[idx] = tIdx - idx
            else:
                waitArr[idx] = 0
        """

        # use Monotonic Stack
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackInd = stack.pop(-1)
                waitArr[stackInd] = i - stackInd

            stack.append((t, i))

        return waitArr
