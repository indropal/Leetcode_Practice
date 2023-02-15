class Solution:
    def addBinary(self, a: str, b: str) -> str:

        Na, Nb = len(a), len(b)

        # adjust for unequal lengths in strings by padding '0' in MSB
        if 0 < Nb - Na:
            a = ("0"*(Nb-Na))+a
        else:
            b = ("0"*(Na-Nb))+b
        
        # print(a, b)

        def sumBinary(aBin, bBin, prevCarry):
            sumBin = 0
            carryBin = 0

            if aBin and bBin:
                # if both bits are set
                sumBin = (int(aBin) ^ int(bBin)) ^ int(prevCarry)
                carryBin = 1 # set this bit as both binary bits are set
            
            elif aBin or bBin:
                # if either bits are set
                sumBin = (int(aBin) ^ int(bBin)) ^ int(prevCarry)
                carryBin =  1 if ((int(aBin) ^ int(bBin)) and int(prevCarry)) else 0
            
            else:
                # if both are not set
                sumBin = (int(aBin) ^ int(bBin)) ^ int(prevCarry)
                carryBin = 0

            # print(aBin, bBin, preCarry, sumBin, carryBin)

            return (sumBin, carryBin)

        preCarry = 0
        ans = ""
        for i in range(max(Nb, Na)-1, -1, -1):
            binSum, binCarry = sumBinary(int(a[i]), int(b[i]), preCarry)
            preCarry = binCarry
            ans = str(binSum) + ans

        if preCarry:
            # adjust for remaining Carry bit
            ans = str(preCarry) + ans

        return ans