import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        # This solution requires Auxillary space via Hasmap (time: O(n))
        # There could be a better solution which needs constant space

        hashMap = collections.defaultdict(int)
        maxFreq, ans = 0, 0

        for n in nums:
            hashMap[n] += 1
        
        for k, v in hashMap.items():
            if maxFreq < v:
                ans = k
                maxFreq = v
        
        return ans
        """

        # An alternative solution is by using Boyer-moore's voting algorithm
        # and changing it a bit
        #
        # As we iterate through the array we are guaranteed there exists a number
        # such that it appears more than [n/2] times in the array. Therefore per
        # number selected at a time, if we consider a value of +1 for the selecte number 
        # and the rest of the nummbers assigned a value of -1 ~ using these we update the count
        # we will eventually have cases where the count equals 0, signifying that the chosen candidate
        # number might not be the majority element & select he next available number as candidate with 
        # value +1.
        # Eventually for majority element, the number will be selected many times which guaratees it
        # ending up being selected by the time we end looping through the array.
        #
        # This is the intuition behind Boyrer-Moore's imporvised voting solution
        # Space: O(1) | Time: O(N)

        count, candidate = 0, None

        for n in nums:
            
            if count == 0:
                candidate = n
                count += 1
            
            elif n == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate