class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        N, currRow = len(s), 0
        # rowTrack, reverse = [], False
        hashMap, ans = {}, ""
        reverse = False

        # Algo:
        # We count the  row number per iteration of each element in the string - the row number
        # starts from 0 and ends at 'numRows-1' and then decrements till 0 for subsequent iterations after 
        # which it again increments from 0 till 'numRows-1' & then back to 0 again i.e.
        # the rowCount increases & decreases alternatively depending on when counter has arrived at 'numRows-1'
        # value. The idea is to assign each character in string to a row number in the zig zag path and then
        # to collate all the characters with the same row number together and present it as the answer.
        #
        # It is guaranteed that the first 'numRows' elements will be within 0 ~ numRows-1
        # hence, we can iterate through the elemnts & obtain a hashmap where each row maps to
        # the sequence of string elements per row & then we concatenate it -> the keys are the
        # row numbers and the first 'numRows' elements will be sorted hence the keys in dictionary is
        # guaranteed to be sorted.

        for i in range(N):

            if (i!=0) and (i%(numRows-1)==0):
                reverse = not reverse
            
            # We dont need to store 'currRow' in list ~directly store in HashMap
            # rowTrack.append(currRow)
            
            # include in answer mapped to corresponding row
            if not hashMap.get(currRow):
                hashMap[currRow] = ""
            hashMap[currRow] += s[i]

            currRow = currRow + 1 if not reverse else currRow - 1

        # print(hashMap); # print(rowTrack)

        for v in hashMap.values():
            ans += v

        return ans