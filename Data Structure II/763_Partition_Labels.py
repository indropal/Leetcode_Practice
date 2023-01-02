class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Obtain a Hash-table where each of the keys (letters) is mapped to the Last 
        # occuring index of the key/letter
        lastIdx = {}
        ans = []

        for i, l in enumerate(s):
            if not lastIdx.get(l):
                lastIdx[l] = i
            lastIdx[l] = max(i, lastIdx[l])
        
        print(lastIdx)
        # traverse through the entire string and at each iteration maintain a 'size' variable &
        # 'last-index' variable, where the last-index gives the last-possible index of any letter
        # seen so far. The greedy way to go about this is that we always pick the maximum last-index
        # and break the partition until then. Once we reach the the max. index for all letters seen till
        # now, we push the 'size' variable which we have been incrementing at every step in traversal, reset
        # the size & move the 'last-index' & update it to the letter of the next index.
        
        size, i, lIdx = 0, 0, 0 # intiialize variables

        while i < len(s):
            l = s[i]
            size += 1
            lIdx = max(lIdx, lastIdx[l]); #print(l, size, i, lIdx)

            # If we've reached the max. possible last-index of occurence for all the letters seen so far
            # we push the 'size' var into ans & reset it 0 and continue to the next iteration
            if i == lIdx:
                ans.append(size)
                # print("Reached Last Index: ", lIdx, "size: ", size)
                size = 0

            i += 1

        return ans
