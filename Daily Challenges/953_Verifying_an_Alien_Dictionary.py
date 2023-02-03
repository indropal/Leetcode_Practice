class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def orderIdx(ele):
            return order.index(ele)

        # get the index of each character in string from respective order
        # if they are more then remove them
        N = len(words)

        for i in range(N-1):
            j = i+1

            # word[i] should be smaller than word[j]
            Nw = min(len(words[i]), len(words[j]))
            t = 0
            # check the first letters, if first letters are strictly in lexicographical order
            # (i.e. non-equal letters) then move to next comparison 
            if (orderIdx(words[i][t]) < orderIdx(words[j][t])):
                continue
            elif (orderIdx(words[i][t]) != orderIdx(words[j][t])):
                # if the first letters aren't equal and they didn't follow the order
                # return false
                return False

            # if the first letters are the same, then check the other letters
            t += 1
            while (t < Nw) and (orderIdx(words[i][t]) <= orderIdx(words[j][t])):
                if orderIdx(words[i][t]) < orderIdx(words[j][t]):
                    # if the letters are strictly in lexicographic order then no need
                    # to compare further ~ skip to next word
                    break
                t += 1
            
            # follow up after the break statement i.e. letters in between are in lexicographic order
            if (t!=Nw) and (orderIdx(words[i][t]) < orderIdx(words[j][t])):
                continue

            # print(words[i][t-1], words[j][t-1])

            if (t != Nw) or ((t == Nw) and (len(words[j]) < len(words[i]))):
                return False
        
        return True