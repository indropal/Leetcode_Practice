class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        > The algorithm is to use Backtracking to find all possible subsequences
          from the array which are increasing in nature.
        > The solution follows the usual Backtracking template
        """
        
        """
        # The current solution involves using a Set (Python implements a hashSet)
        # in order to prevent the presenece of duplicates in the answer array
        #
        # Alternative solution is to use a list as answer
        #
        # Both solutions are fine.

        ans = set() # use set to not worry about duplicates
        N = len(nums)

        if N == 1:
            return ans
        
        if N == 2:
            if nums[0] < nums[1]:
                ans.add((nums[0], nums[1]))
                return ans
        
        # Use Backtracking to find all possible subsequences & pick the ones
        # which are increasing in nature

        def backTrack(start, tmpAns):
            if len(tmpAns) > 1:
                ans.add(tuple(tmpAns))
            
            lastEle = tmpAns[-1] if 0 < len(tmpAns) else float("-inf")

            for i in range(start, N):
                if lastEle <= nums[i]:
                    tmpAns.append(nums[i])

                    # call backtrack with the next index as starting index
                    # to consider all possible subsequences from that index
                    backTrack(i+1, tmpAns)
                    
                    tmpAns.pop()

        backTrack(0, [])

        return ans
        """

        # using the answer array as a normal Python List
        ans = []
        N = len(nums)

        if N == 1:
            return ans
        
        if N == 2:
            if nums[0] < nums[1]:
                ans.append([nums[0], nums[1]])
            return ans
        
        def backTrack(startIdx, tmpAns):

            if 1 < len(tmpAns):
                ans.append(tmpAns[:])
            
            # Keep track of the last element in the subsequence
            lastEle = tmpAns[-1] if tmpAns else float("-inf")
            
            # keep track of the numbers already seen to avoid duplicates
            seenNums = set()

            for i in range(startIdx, N):

                if nums[i] in seenNums:
                    # the number has already been considered - we
                    # omit the number to avoid duplicates
                    continue
                
                if lastEle <= nums[i]:
                    tmpAns.append(nums[i])
                    # Consider all subsequences from the next index by
                    # including the current element as it satisfies inc. subseq. constraint
                    backTrack(i+1, tmpAns)

                    # Pop the included element to consider subsequences without current element present
                    tmpAns.pop()
                
                # include nums[i] in seen as it has been considered already
                seenNums.add(nums[i])
        
        backTrack(0, [])

        return ans