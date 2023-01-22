class Solution:

    def isPallindrome(self, s: str, left: int, right: int) -> bool:
        # check if the substring in [left, right] (inclusive) is a pallindrome or not
        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True


    def partition(self, s: str) -> List[List[str]]:

        N = len(s)

        # base case when the length of string is one
        if N == 1:
            return [[s]]
        
        # a pallindrome could be of length 1 till N ~we want to generate all possible
        # pallindromes in the string
        #
        # Generate all possible partitions of the string & check if the generated partition
        # string is a pallindrome.
        ans = []
        tmpAns = [] # store the current partition / temporary

        # This Backtracking is very similar to Depth-First-Search
        def backTrack(currIdx):
            if N <= currIdx:
                # we have all valid partitions & no more characters to add into the answer
                # we store & return the answer
                ans.append(tmpAns[:])
                return
            
            # if we haven't reached the base-case i.e. the end of string, we have to iterate through
            # each character in the string. The partition begins from "currIdx" & will end at every possible
            # character following it till the end of the string for which we'll have to check if it is a
            # pallindrom or not

            for i in range(currIdx, N):

                # check if the substring created from the start of the partition till the current iterating index
                # is a pallindrome or not ~ if a pallindrom then include into ans or else continue the iteration
                # while calling the backtracking function
                if self.isPallindrome(s, currIdx, i):
                    # if it is a pallindrome - make the partition & add substring into ans
                    # i.e. new partition from currIdx till i+1 i.e. include the ith character
                    tmpAns.append(s[currIdx:i+1])

                    # make backtrack call for the next partition
                    backTrack(i+1)

                    # consider option of not including the substring
                    tmpAns.pop()
        
        backTrack(0)

        return ans