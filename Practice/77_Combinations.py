class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = set()
        
        if n == 1:
            return [[1]]
        
        if k == 1:
            return [[i] for i in range(1, n+1)]
        
        if k == n:
            return [[i for i in range(1, n+1)]]
        
        # use backtrack to find all combinations
        numArr = [i for i in range(1, n+1)]
        tmpAns, N = [], len(numArr)
        
        def backTrack(i, tmpAns):
            
            if len(tmpAns) == k:
                # the populated subset is of k length ~ include into answer
                nonlocal ans
                ans.add(tuple(tmpAns[:])); #print(tmpAns[:])
                
                return

            # We cannot choose the same number again, thats why looking
            # ahead into the array as the num array is sorted            
            while i < N:

                # inlcude into tmpAns & backtrack
                tmpAns.append(numArr[i])
                
                # backtrack
                backTrack(i + 1, tmpAns)
                
                # remove the chosen num to consider other elements in selected subset
                tmpAns.pop()
                
                i += 1
        
        backTrack(0, tmpAns)
        
        return ans