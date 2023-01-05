class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Iterate the array in sliding windows of length of 10 
        # store these arrays in a HashMap / Python Dict
        # Search for the sequence if it exists in the HashMap
        # - if it doesn't, include it and update its occurence frequency to 1
        # - if it was pre-existent, the increment its occurence frequency
        #
        #  return the sequences with frequency greater than 1
        """
        hashMap = {}
        startIdx, endIdx = 0, 10
        N = len(s)

        while endIdx <= N:
            
            # print(s[startIdx:endIdx], len(s[startIdx:endIdx]))
            if not hashMap.get(s[startIdx:endIdx]):
                hashMap[s[startIdx:endIdx]] = 0 # if not existent then increment frequency
            hashMap[s[startIdx:endIdx]] += 1 # increment frequency
            
            startIdx += 1
            endIdx += 1

        return [k for k, v in hashMap.items() if 1 < v]
        """

        # Using Hash-Set is alot more faster than using HashMap / Python Dictionaries
        seen, res = set(), set() # initialize hash Set

        # for each visited seq. of string, store in the 'seen' set ~but check if it is already existent or not
        # if the string is already seen in HashSet, then store the string in 'result' set
        # else if not already seen, then include in 'seen' set
        
        for l in range(len(s)-9):
            cur = s[l: l+10]

            if cur in seen:
                res.add(cur)
            seen.add(cur)

        return list(res)
