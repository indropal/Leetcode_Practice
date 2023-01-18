class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        > The idea is to use kadan's algorithm to find the maximum subarray

        Intuition:
        
        - It'll be complicated to take into account the circular nature of
          the array when shifting the window, therefore a simplification would be
          to consider a minimum sum subarray in the entire array & remove it to
          obtain a maximum sum sub array while also taking into consideration the
          usual maximum sum subarray via Kadan's.
        
        - Consider when we remove the min. subarray from the middle of the array;
          what remains is the the outer portions of the array which are connected via
          circular property of array which possibly contains the max subarray.
          Running Kadane's usual max subarray would take a portion of this remainder subset
          of array, giving the max sum or the subtraction of Minimum sum subarray from
          the total sum of all elements in array gives the max sum in subarray with cyclic
          connection.

        """
        N = len(nums)

        # Get the total sum of elements in the array
        tmpTot = sum(nums); # print(nums, tmpTot)

        # Declare variables to keep track of the subarray
        # with maximum & minimum sums respectively
        maxSum, maxTot = float('-inf'), 0
        minSum, minTot = float('inf'), 0

        # Use kadane's algorithm to find the maximum & minimum
        # sum subarrays respectively
        for i, n in enumerate(nums):
            maxTot += n
            minTot += n
            
            if maxTot < n:
                # if the current element is larger than the total (inclusive of element)
                # then restart the subarray and also the tally for the total
                maxTot = n
            
            if n < minTot :
                minTot = n

            # since the array is circuilar in nature, keep track of the index which is the
            # end of the subarray
            if maxTot > maxSum:
                maxSum = maxTot
            
            if minTot < minSum:
                minSum = minTot

            # print(minTot, maxTot, minSum, maxSum)

        # For the final sum - keep track of the minimum Sum & maximum sum
        # Use the minimum-Sum to find the subarray with the minimum value &
        # subtract it from the total sum of all the elements in the array
        #
        # > The idea is that if we exclude the subarray with minimum sum from the
        #   entire array - there should exist a subarray with maximum sum. We use
        #   this intuition to obtain our result by taking maximum of subtracting the
        #   total sum of all elements in the array with subarray with minimum sum &
        #   maximum sum using kadan's algorithm ~ the reason being that there could be
        #   a sccenario where the contributing elements might not be contiguous
        #
        # > If the sum of all elements in the subarray is equal to the minimum sum subarray
        #   then there must be bits of elements in array where sum is equal to zero. Hence
        #   for such a scenario answer is just the maximum subarray sum by Kadane's

        ans = None
        
        if tmpTot == minSum:
            ans = maxSum
        else: 
            ans = max(maxSum, tmpTot - minSum)

        return ans