class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        firstLow, secondLow = False, False
        ans = True

        if len(word) == 1:
            return ans
        
        # Check the forst 2 letters as it determines if the following letters will ALL have to be
        # in upper-case or all of them have to be in lower-case
        if (65 <= ord(word[0])) and (ord(word[0]) <= 90):
            firstLow = False
        else:
            firstLow = True
        
        if (65 <= ord(word[1])) and (ord(word[1]) <= 90):
            secondLow = False
        else:
            secondLow = True

        if firstLow and not secondLow:
            # first character is lower-case & second character is upper-case
            # then its invalid & answer is false
            ans = False
            return ans

        for l in word[2:]:
            if firstLow and secondLow and ((65 <= ord(l)) and (ord(l) <= 90)):
                # all the letters have to be in lower-case
                ans = False
                break

            if (not firstLow) and (secondLow) and ((65 <= ord(l)) and (ord(l) <= 90)):
                # First letter is capital and second letter is lower-case ~ then all of them have to be lower-case
                ans = False
                break

            if (not firstLow) and (not secondLow) and not ((65 <= ord(l)) and (ord(l) <= 90)):
                # Both are in Caps - then all of them have to be in caps
                ans = False
                break
        
        return ans