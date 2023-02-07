class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freqHash = {}
        ans, tmpAns = 0, 0
        r, l = 0, 0
        N = len(fruits)

        while r < N:

            # include the fruit from new tree into Freq. Hash
            if not freqHash.get(fruits[r]):
                # if new fruit has been encountered for first time..
                freqHash[fruits[r]] = 0
            freqHash[fruits[r]] += 1
            tmpAns += 1

            while 2 < len(freqHash):
                # there's a new fruit that has been introduced into basket
                # it exceeds the atmost 2 distinct types of fruit possible 
                # in basket 
                #
                # There's a fruit at the left most index in the sliding window
                # - we want to keep getting rid of contiguous such fruits from our window
                # until we encounter a non-similar fruit from the left.
                # Update the freq. hash ~if the freq. is 0 then pop the fruit from Hashmap
                
                f = fruits[l] # get the leftmost fruit
                freqHash[f] -= 1
                tmpAns -= 1

                # update the left pointer
                l += 1

                if not freqHash[f]:
                    # if the count of the left-most fruit has reached '0', then remove from HashMap
                    freqHash.pop(f)

            ans = max(ans, tmpAns)
            r += 1
        
        return ans