class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        N, ans = len(nums), 0
        prefSum = 0
        """
        Algorithm: 

        > The intuition is to consider the prefix sum of the array. While iterating through
          the array update a variable by adding each element of the array per iteration
          and maintain a hashmap of the number of occurences with the remiander obtained by dividing the
          prefix-sum by 'k'.

        > The idea is that for a prefix sum which gives a remainder of say 'R' at index 'i' & the same remainder
          'R' at index j where i < j when prefix sum is divided by 'K' - in between the indices i & j there exists
           a subarray such that its sum is divisible by K.

        > We are not explicitly counting the number of subarrays while iterating through the array, rather
          we are counting the number of times the remainder 'R' (0 <= R < K) occurs with each iteration & updating
          the count of the occurence for that remainder as well. Also, We initialize the remainder-frequency-Hashmap
          with reminader of '0' assigned freq. of 1 as this is a special case scenario for handling instances where the
          subarray perfectly is divisible by 'k' & we have an initial freq. value to retrieve from hashMap
        
        > At each instance of iteration, we update the prefix sum by adding the current element to it, the 
          remainder-freq-hashmap by updating the subarray-count with hashmap-stored-value of "prefix-sum % K"
          and then incrementing freq. of the remainder of "prefix-sum % K". We do this as before that specific index
          we will have exactly "prefix-sum % K" equivalent freq. number of subarrays which are present that add upto
          a value which is a multiple of 'K' since the last index we obtained a value of "prefix-sum % K" remainder.
        """

        hashRemainder = {0 : 1} # handle edge-case where remainder is 0

        if N == 1:
            # handle instance where number of elements in array is 1
            ans = 1 if sum(nums)%k==0 else 0
            return ans

        for n in nums:
            # while iterating through the array maintain a prefix sum i.e. rolling sum 
            prefSum += n

            if not hashRemainder.get(prefSum%k):
                # if the remainder when dividing with K DOES NOT exists in the hashMap ~ we encounter
                # it for the first time - include it into the Hashmap
                hashRemainder[prefSum%k] = 1
            else:
                # if the remainder exists in the hashMap - the freq. of it is the number of subarrays
                # whose sum is equal to multiple of K since the last index where the prefix sum left
                # remainder value when dividing by K 
                ans += hashRemainder[prefSum%k]
                hashRemainder[prefSum%k] += 1 # update the freq. count for the remainder
        
        # print(hashRemainder)
        return ans

