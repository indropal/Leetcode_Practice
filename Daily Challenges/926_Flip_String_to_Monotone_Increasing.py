class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        > DP technique used. The idea is that until the first occuring 1 in the string
          all the characters can be 0. when we find a 1 or rather the first 1, we should
          consider whether to flip the present '1' or flip all the previous occuring '0's
          before it.
          
          Flip the 0's before the 1
          V   VV 
          0-- 00 --- 1 -----
                     ^
                     Or flip the 1
          
          We should make the minimum number of flips.
          The idea is that while iterating, if the element is '1', then increase the counter of
          1 to keep track of the number of 1's to flip inorder to maintain monotone inc. sequence.
          Further, if the element is 0, then increment the counter for zero by 1 to keep track of whether
          to flip zero or not ~ which ever gives minimum out of flipping 1 or 0.
        """
        ans, one = 0, 0 
        
        # 'ans' keeps track of flipping the zeros per iteration as well as
        # keeps tally of the minimum number of flips to maintain monotone inc. seq.
        #
        # 'one' ~ keeps track of the ones which might be flipped
        for ele in s:
            if ele == '1':
                # increment one counter
                one += 1
            else:
                # keep tally of the minimum number of flips out of 1 or 0
                # if the current element is 0 ~ then only update the 'ans' var
                # as we'd only need to flip if there's a '0' occuring after a
                # '1' to maintain monotonicity.
                ans = min(one, ans+1)
        
        return ans