class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N1, N2 = len(s1), len(s2)

        if N2 < N1:
            return False
        
        # take a window of length N1 & check if the hashed freq. maps match or not
        hashOrig, ans = {}, False

        # store the freq. hash of String 1
        for e in s1:
            if not hashOrig.get(e):
                hashOrig[e] = 0
            hashOrig[e] += 1
        
        def check(hashOrig, tempHash):
            flag = True

            for k, v in hashOrig.items():
                if (not tempHash.get(k)) or (tempHash[k] != v):
                    flag = False
                    break
            
            return flag
        
        # populate N1 length of char in freq. Hash & slide the window
        hashTemp = {}
        start, end = 0, N1-1 # start & end indices of window
        # populate temp Hash
        for i in range(start, end+1):
            if not hashTemp.get(s2[i]):
                hashTemp[s2[i]] = 0
            hashTemp[s2[i]] += 1
        
        # slide the window one step ahead
        start += 1
        end += 1

        if check(hashOrig, hashTemp):
            # if both equal then return True
            return True

        while end < N2:
            # remove the prev. window's starting character freq. count
            hashTemp[s2[start-1]] -= 1
            if not hashTemp.get(s2[end]):
                hashTemp[s2[end]] = 0    
            hashTemp[s2[end]] += 1

            if check(hashOrig, hashTemp):
                # if both equal then return True
                return True

            end += 1
            start += 1
        
        return ans