class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        freqP, ans = {}, []
        N = len(s)

        if N < window:
            # then an anagram cannot exist in 's'
            return ans
        
        # get freq. map of all chars in 'p'
        for e in p:
            if not freqP.get(e):
                freqP[e] = 0
            freqP[e] += 1
        
        # take a sliding window of length 'window' & iterate through 's' with this window
        # if the frq. of the elements match ~ then we have the answer
        start, end = 0, window-1
        i = start
        windowFreq = {}

        # populate the freq of elements for the first 'window' size of characters
        while i <= end:
            
            if not windowFreq.get(s[i]):
                windowFreq[s[i]] = 0
            windowFreq[s[i]] += 1

            i += 1
        
        # currently the window starts at 0 & ends at 'window-1'.
        # as we move the window we remove the previous first elemnt in the prev. window from Freq. Map
        # & include the new last element of window in the Freq. Map

        # check if 'windowFreq' & 'freqP' are equal
        def check(wFreq ,freqP):
            flag = True
            for k, v in freqP.items():
                if (not wFreq.get(k)) or (wFreq[k] != v):
                    flag = False
                    break
            return flag
        
        if check(windowFreq, freqP):
            ans.append(start) # include starting index of 
        
        # slide to the next window
        start += 1
        end += 1

        while end < N:
            # remove the count of the start-ing element of previous window snippet
            windowFreq[s[start-1]] -= 1
            # include the count of the new end-ing element of new window snippet
            if not windowFreq.get(s[end]): 
                windowFreq[s[end]] = 0
            windowFreq[s[end]] += 1

            # check if the freq. maps are equal or not
            if check(windowFreq, freqP):
                ans.append(start)
            
            start += 1
            end += 1
        
        return ans