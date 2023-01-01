class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        N = len(s)
        # get the frequency map of all the letters & choose the ones which
        # have even frequency

        hash = collections.defaultdict(int)
        odd = 0

        for letter in s:
            hash[letter] += 1

        # Check the Element-Frequency Dictionary
        # print(hash.items())

        for k, v in hash.items():
            if v%2 == 0:
                # All elements with even frequency get included
                ans += v
            elif (2 <= v) and (v%2 != 0):
                # All elements with odd freq. but greater than 2 get even number of them included
                # Include all of the letters except for 1
                ans += (v - 1)
                odd += 1 # we need to keep count of the number of letters which occur exactly once
            else:
                odd += 1 # we need to keep count of the number of letters which occur exactly once

        # If there is an element which occurs exactly once, keepit at the middle of the pallindrome
        ans = ans +1 if (ans <= N-1) and (0 < odd) else ans

        return ans


