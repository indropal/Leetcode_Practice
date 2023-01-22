class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) < 4 or 12 < len(s):
            # there can be atmost 3 dots & 4 integers
            # each of these integers have to be less than 256 i.e.
            # each integer can have atmost 3 digits & there can be atmost 4 integers
            # so total num of digits is 3X4 = 12 digits. Any string with more than 12
            # digits will result in invalid IP address
            return []
        
        if len(s) == 4:
            return [".".join([char for char in s])]
        
        ans = []
        tmpAns, N = "", len(s)

        # In each segment of IP address between dots we can have an integer which
        # is atmost 3 digits inlength and has value of atmost 255
        # So per back track step, our decision lies whether to include any of the
        # 3 digits ahead of the current index and to progressively include them to see if they
        # meet the constraints
        def backTrack(idx, dots, tmpAns):
            # 'idx' ~ the current Index we are in
            # "dots" ~ the number of dots we have added into our temp ans so far
            # "tmpAns" ~ candidate IP address created

            if dots == 4 and idx == N:
                # a valid IP address can have atmost 3 dots in it
                # the 4th dot here is the trailing dot which we have to remove
                #
                # we have currently reached the end of the provided integer string
                ans.append(tmpAns[:-1])
                return
            
            for j in range(idx, min(N, idx+3)):
                # checking bounds so that 'j' does not overshoot N
                if (int(s[idx:j+1]) <= 255) and (idx==j or s[idx]!= "0"):
                    # checking for leading zeros or valid integer
                    # include into temp answer & backtrack
                    l = len(tmpAns)
                    
                    tmpAns += (s[idx:j+1] + ".")

                    # backtrack
                    backTrack(j+1, dots+1, tmpAns)

                    tmpAns = tmpAns[:l]
            
        backTrack(0, 0, tmpAns)

        return ans
