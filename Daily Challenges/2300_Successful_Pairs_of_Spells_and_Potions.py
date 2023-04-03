class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort potions array ~ Spells cant be sorted as the answer array is dependent on the
        # ordering of spells
        potions = sorted(potions)
        N_potions = len(potions)
        
        # for each element in spells, perform B-search on potions to obtain the other number to
        # get product
        ans = []

        # Binary search for the first number that is greater or equal to the number which we're 
        # searching for.
        def bSearch(start, end, arr, target, spell):
            
            idx = N_potions
            while start <= end:
                mid = start + (end - start)//2

                if target <= spell*arr[mid]:
                    idx = mid
                    end = mid-1
                else:
                    start = mid+1
            
            # we want the first number which is greater than or equal to the target
            # since the array is zero-indexed, we get the number of potions which
            # are invlaid equal to the index value itself i.e. left of the index 'idx'
            # Therefore the number of valid potions is N - idx
            return idx
            
        # ans = [ bSearch(0, N_potions-1, potions, success//sp) for sp in spells]
        for sp in spells:
            tmpAns = 0

            tmpIdx = bSearch(0, N_potions-1, potions, success, sp)
            tmpAns = N_potions - tmpIdx

            ans.append(tmpAns)

        return ans


