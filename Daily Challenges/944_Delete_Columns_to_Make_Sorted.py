class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # all string are of equal length, so get the length of first string
        # to get the number of columns to process
        Nc = len(strs[0])
        ans, i = 0, 0

        while i < Nc:
            # for the ith column i.e. ith letter in string, iterate through all the strings
            # checking that the ASCII of the ith letter of consecutive strings is increasing or
            # atleast equal but never follows a decreasing trend - if ASCII is decreasing
            # then we need to delete the column , thus incrementing the answer
            prev = -1
            for s in strs:
                if ord(s[i]) < prev:
                    ans += 1
                    break
                prev = ord(s[i])
            i+=1
        
        return ans