class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) <= 1:
            return [strs]

        tmpStrs = [ (''.join(sorted(s)), i) for i, s in enumerate(strs)]
        tmpStrs = sorted(tmpStrs, key=lambda r: r[0]); #print(tmpStrs)
        
        i, j, N = 0, 1, len(tmpStrs)
        ans = []

        while j < N:
            while (j < N) and (tmpStrs[i][0] == tmpStrs[j][0]):
                j += 1
            
            # tmpAns = [ strs[e[-1]] for e in tmpStrs[i:j]] #don't need to declare an extra memory-container
            ans.append([ strs[e[-1]] for e in tmpStrs[i:j]]); # ans.append(tmpAns)
            i = j
            j = i+1

            # Corner case if we are pointing beyond the last element
            if (i == N-1):
                # print(strs[tmpStrs[i][-1]])
                ans.append([strs[tmpStrs[i][-1]]])

        return ans #[[""]]
